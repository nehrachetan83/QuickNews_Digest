import worldnewsapi

# Initial SDK configuration
newsapi_configuration = worldnewsapi.Configuration(api_key={'apiKey': 'fc585c57f0f6471fa50ad266445d3f5c'})

try:
	newsapi_instance = worldnewsapi.NewsApi(worldnewsapi.ApiClient(newsapi_configuration))

	max_results = 50   # replace with your maximum
	offset = 0
	all_results = []

	while len(all_results) < max_results:

		request_count = min(100, max_results - len(all_results)) # request 100 or the remaining number of articles

		response = newsapi_instance.search_news(
			text='india',
			source_countries='in',
			language='en',
			earliest_publish_date='2024-02-12',
			latest_publish_date='2024-04-15',
			sort="publish-time",
			sort_direction="desc",
			# min_sentiment=-0.8,
			# max_sentiment=0.8,
			offset=offset,
			number=request_count)

		print("Retrieved " + str(len(response.news)) + " articles. Offset: " + str(offset) + "/" + str(max_results) +
			  ". Total available: " + str(response.available) + ".")

		all_results.extend(response.news)
		offset += 100


except worldnewsapi.ApiException as e:
	print("Exception when calling NewsApi->search_news: %s\n" % e)


# for article in all_results:
    # print("\nTitle: " + str(article.title))
    # print("Author: " + str(article.authors))
    # print("URL: " + str(article.url))
    # print("Sentiment: " + str(article.sentiment))
    # print("Text: " + str(article.text[:min(5000,len(article.text))]),end="\n") 
    # print(len(str(article.summary).split()),end="\n") 

print(all_results[35].text)
# print(all_results[35].image)