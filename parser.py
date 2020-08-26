from html.parser import HTMLParser

class customHTMLParser( HTMLParser ):
	def handle_starttag(self, tag, attrs):
		print( "Encountered a start tag: ", tag)
	def handle_engtag(self, tag, attrs):
		print( "Encountered an end tag: ", tag)
	def handle_data(self, tag, attrs):
		print( "Encountered some data: ", data)

parser = customHTMLParser()
parser.feed("<div class=\"class_here\"></div>")
