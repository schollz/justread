# From http://rodp.me/2015/how-to-extract-data-from-the-web.html
import time
import sys
import uuid
from collections import Counter
from requests import get
from lxml import html
from unidecode import unidecode
import urllib
import lxml.html



def getDoc(url):
	t = time.time()
	r = get(url)
	redirectUrl = str(uuid.uuid3(uuid.NAMESPACE_DNS, str(r.url)))[0:5]


	parsed_doc = html.fromstring(r.content)




	parents_with_children_counts = []
	parent_elements = parsed_doc.xpath('//body//*/..')
	for parent in parent_elements:
		children_counts = Counter([child.tag for child in parent.iterchildren()])
		parents_with_children_counts.append((parent, children_counts))

	parents_with_children_counts.sort(key=lambda x: x[1].most_common(1)[0][1], reverse=True)

	docStrings = {}

	for i in range(10):
		docString = ""
		numLines = 0
		for child in parents_with_children_counts[i][0]: # Possibly [1][0]
			tag = str(child.tag)
			if tag == 'font':
				tag = 'p'
			try:
				startTag = "<" + tag + ">"
				endTag = "</" + tag + ">"
			except:
				startTag = '<p>'
				endTag = '</p>'
			if "script" in startTag or "header" in startTag or "footer" in startTag:
				continue
			try:
				newString = startTag + " ".join(str(child.text_content().encode('utf-8')).split()) + endTag + "\n"
				if "<script>" in newString:
					continue
				if len(newString) > 10000 or len(newString)<14 or '{ "' in newString:
					continue
				print(len(newString))
				if len(newString) > 100:
					numLines += 1
				docString += newString
			except:
				pass
		docStrings[i] = {}
		docStrings[i]['docString'] = docString
		docStrings[i]['numLines'] = numLines

	bestI = 0
	bestNumLines = 0
	for i in range(len(docStrings)):
		print(docStrings[i]['numLines'])
		if docStrings[i]['numLines'] > bestNumLines:
			bestI = i
			bestNumLines = docStrings[i]['numLines']

	docString = docStrings[bestI]['docString']

	if len(docString)<100:
		docString="<h1>There is no content on this page.</h1>"

	title = parsed_doc.xpath(".//title")[0].text_content().strip()
	try:
		description = parsed_doc.xpath(".//meta[@name='description']")[0].get('content')
	except:
		description = ""
	url = r.url
	timeElapsed = int((time.time()-t)*1000)
	return {'title':title,'description':description,'url':url,'timeElapsed':timeElapsed,'content':docString.decode('utf-8')}

#print(getDoc('http://www.bbc.co.uk/news/entertainment-arts-34768201'))
