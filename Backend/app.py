from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
from transformers import pipeline
import feedparser

app = Flask(__name__)

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Function to fetch and parse the content of an article
def fetch_article_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    article_text = ' '.join([p.get_text() for p in soup.find_all('p')])
    return article_text

@app.route('/', methods=['GET'])
def top_news():
    # URL for Google News top stories RSS feed
    rss_url = "https://news.google.com/rss?hl=en-US&gl=IN&ceid=US:en"

    # Parse the RSS feed
    feed = feedparser.parse(rss_url)
    articles = []

    for entry in feed.entries:
        article = {
            'title': entry.title,
            'link': entry.link,
            'source': entry.source.title if 'source' in entry else 'Unknown'
        }
        articles.append(article)

    summarized_articles = []
    count =0
    for article in articles:
        if(count==10):
            break
        content = fetch_article_content(article['link'])
        if content:
            content_length = len(content.split())
            try:
                # Adjust summarization parameters based on content length
                max_length = min(100, content_length - 1)
                min_length = max(10, min(100, int(content_length * 0.1)))
                
                if content_length > min_length:
                    summary = summarizer(content, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
                    summarized_articles.append({
                        'title': article['title'],
                        'link': article['link'],
                        'source': article['source'],
                        'summary': summary
                    })
                    count=1+count
                else:
                    # If content is too short to summarize, skip summarization
                    summarized_articles.append({
                        'title': article['title'],
                        'link': article['link'],
                        'source': article['source'],
                        'summary': content
                    })
                    count=1+count
            except Exception as e:
                print(f"Error summarizing article {article['link']}: {e}")

    return jsonify(summarized_articles)

if __name__ == '__main__':
    app.run(debug=True)
