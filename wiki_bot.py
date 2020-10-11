# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#											#
# 	This is a bot that utilizes Wikipedia's API to retrieve the introductions	#
# 	of articles by first searching for a topic and finding the most relevant 	#
# 	article. Topics can also be randomly searched. 					#
#											#
# 	Author: Tyler Hooks								#
#											#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # @ @ @ @



import json
import requests

def get_topic_info(topic):
	# Make an API request for a random Wikipedia article.
	if topic == 'random':
		url = f"http://en.wikipedia.org/w/api.php?action=query&generator=random&grnnamespace=0&prop=extracts&format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&indexpageids"
		
	else:	
		# Pulls the topic title from the first Wikipedia article to ensure a page exists. 
		url = f"https://www.google.com/search?q={topic}&as_sitesearch=wikipedia.org&btnI=1"
		search = requests.get(url).url
		subject = search.split('/')[len(search.split('/')) - 1]
		
		# Make an API call to Wikipedia to retrieve article information. 
		url = f"https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&indexpageids&titles={subject}"
	
	page = requests.get(url)
	# The API call returns a JSON document. 
	result = json.loads(page.content)
	# Get the page id, as the API returns a nested JSON document which requires the id for the article as a dictionary key. 
	pageid = result['query']['pageids'][0]
	# Get the article introduction from the JSON document. 
	article = result['query']['pages'][pageid]['extract']
	print("\n\n")
	print(article)
	print("\n")

print("Please enter the topic you would like to learn more about or type 'random' for a random topic. Type 'quit' to exit.\n")
while True:
	try:
		topic = input("Search: ")
		if topic == "quit":
			break
		get_topic_info(topic)
	except:
		print("No information is available for this topic.\n")
