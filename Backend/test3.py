import requests
from bs4 import BeautifulSoup

# List of news items with titles and links from the RSS feed
news_items = [
    {
        'title': "India election results 2024: Modi's BJP ahead but opposition makes inroads",
        'link': "https://news.google.com/rss/articles/CBMiamh0dHBzOi8vYXBuZXdzLmNvbS9hcnRpY2xlL2luZGlhLWVsZWN0aW9uLXJlc3VsdHMtMjAyNC1sb2stc2FiaGEtbW9kaS1ianAtNzg5M2VmZWNjODNmYTgyMjVhNjExZjE3NGU2NDIwZWXSAQA?oc=5",
        'source': "The Associated Press"
    },
    {
        'title': "Election Results 2024 Highlights: Lok Sabha Elections 2024, Lok Sabha Election Results, BJP, Congress, INDIA Alliance, Narendra Modi, Rahul Gandhi",
        'link': "https://news.google.com/rss/articles/CBMiuQFodHRwczovL3d3dy5uZHR2LmNvbS9pbmRpYS1uZXdzL2VsZWN0aW9uLXJlc3VsdHMtMjAyNC1saXZlLXVwZGF0ZXMtbG9rLXNhYmhhLWVsZWN0aW9ucy1yZXN1bHRzLTIwMjQtYmpwLWNvbmdyZXNzLWluZGlhLWFsbGlhbmNlLW5hcmVuZHJhLW1vZGktcmFodWwtZ2FuZGhpLXdpbnMtd2F5YW5hZC1yYWViYXJlbGktNTgxMTA2N9IBAA?oc=5",
        'source': "NDTV"
    },
    {
        'title': "BJP’s ‘400-paar’ hits INDIA wall, needs allies to govern",
        'link': "https://news.google.com/rss/articles/CBMifWh0dHBzOi8vd3d3LnRoZWhpbmR1LmNvbS9lbGVjdGlvbnMvbG9rLXNhYmhhL2VsZWN0aW9uLXJlc3VsdHMtMjAyNC1ianAtZmFsbHMtc2hvcnQtbmVlZHMtYWxsaWVzLXRvLWdvdmVybi9hcnRpY2xlNjgyNTIxOTIuZWNl0gGCAWh0dHBzOi8vd3d3LnRoZWhpbmR1LmNvbS9lbGVjdGlvbnMvbG9rLXNhYmhhL2VsZWN0aW9uLXJlc3VsdHMtMjAyNC1ianAtZmFsbHMtc2hvcnQtbmVlZHMtYWxsaWVzLXRvLWdvdmVybi9hcnRpY2xlNjgyNTIxOTIuZWNlL2FtcC8?oc=5",
        'source': "The Hindu"
    },
    {
        'title': "Lok Sabha Results 2024: Why BJP's top NDA partners may stay with the alliance – and why they might leave",
        'link': "https://news.google.com/rss/articles/CBMiamh0dHBzOi8vaW5kaWFuZXhwcmVzcy5jb20vYXJ0aWNsZS9leHBsYWluZWQvZXhwbGFpbmVkLXBvbGl0aWNzL2xvay1zYWJoYS1yZXN1bHRzLWJqcC1uZGEtcGFydG5lcnMtOTM3MjA3MC_SAQA?oc=5",
        'source': "The Indian Express"
    },
    {
        'title': "India election results: Modi claims victory for alliance",
        'link': "https://news.google.com/rss/articles/CBMiNmh0dHBzOi8vYXBuZXdzLmNvbS9saXZlL2luZGlhLWVsZWN0aW9uLXJlc3VsdHMtdXBkYXRlc9IBAA?oc=5",
        'source': "The Associated Press"
    }
]

# Function to fetch article content
def fetch_article_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Try different methods to find the main article content
        possible_tags = [
            {'name': 'div', 'class_': 'article-content'},
            {'name': 'article'},
            {'name': 'div', 'class_': 'main-content'},
            {'name': 'div', 'class_': 'content'},
            {'name': 'div', 'class_': 'post-content'},
            {'name': 'div', 'id': 'article-body'},
            {'name': 'section'}
        ]

        article_text = ""
        for tag in possible_tags:
            article_div = soup.find(tag['name'], class_=tag.get('class_'), id=tag.get('id'))
            if article_div:
                paragraphs = article_div.find_all('p')
                article_text = "\n".join([para.get_text() for para in paragraphs])
                if article_text.strip():  # Check if the extracted text is not empty
                    break
        
        # If no main content found, try finding all <p> tags in the body
        if not article_text.strip():
            paragraphs = soup.find_all('p')
            article_text = "\n".join([para.get_text() for para in paragraphs])
        
        return article_text
    except Exception as e:
        return f"Error fetching article content: {e}"

# Fetch and print article content for each news item
for item in news_items:
    print(f"Title: {item['title']}")
    # print(f"Link: {item['link']}")
    # print(f"Source: {item['source']}")
    print("Content:")
    article_content = fetch_article_content(item['link'])
    print(article_content)
    print("-" * 40)
