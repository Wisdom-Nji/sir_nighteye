from html.parser import HTMLParser
import requests as htmlRequest

class customHTMLParser( HTMLParser ):
	def handle_starttag(self, tag, attrs):
		print( "Encountered a start tag: ", tag)
	def handle_endtag(self, tag):
		print( "Encountered an end tag: ", tag)
	def handle_data(self, data):
		print( "Encountered some data: ", data)

# Study this link, will tell you how to retrieve the information
# nih_search_string = "https://search.grants.nih.gov/guide/api/data?perpage=25&sort=reldate:desc&from=0&type=active,nosis&parentic=all&primaryic=all&activitycodes=all&doctype=all&parentfoa=all&daterange=08262020-08262020&clinicaltrials=all&fields=all&spons=true&query="
nih_search_string = "https://search.grants.nih.gov/guide/api/data?perpage=1000&sort=expdate:asc&from=0&type=active,notices,nosis&parentic=all&primaryic=all&activitycodes=all&doctype=all&parentfoa=all&daterange=01021991-08272020&clinicaltrials=all&fields=all&spons=true&query="

# htmlFile = open( "sample_html.html", "r")
htmlRequest = htmlRequest.get( nih_search_string )
htmlRequest_json = htmlRequest.json()
# print("htmlRequest", htmlRequest_json)

hits = htmlRequest_json["data"]["hits"]["hits"]
for i in range(len(hits)):
	print( "Title", i, ":", hits[i]["_source"]["title"])
	
# parser = customHTMLParser()
# parser.feed( htmlFile.read() )
