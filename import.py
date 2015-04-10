'''
Project : K-HUB (XML-TO-JSON-Parser)
Date: 2015-10-04
'''
# -\*- coding: utf-8 -\*-
import xml.etree.ElementTree as ET
import csv
import json


#get the details of book
def getBookDetails(book):
	d = {}

	for details in book:
		item = str(book.find(details.tag).text)
		d[details.tag] = item

	return d

#get BookAttributes
def getBookAttributes(book):
	line = []
	for details in book:
		line.append(str(details.tag))
	f.writerow(['\t'.join(line)])

#get the data for each book
def getBooks(itemName):
	d = {}
	dictionaries=json.loads(json.dumps([dict(book=getBookDetails(book)) for book in root.iter(itemName)]))
	return dictionaries
	

#MAIN######################################################

j = open('thesis.json','w')


#parse the XML file
tree = ET.parse('99.xml')

#obtain root
root = tree.getroot()

data ={}
data['books'] = (getBooks ('book'))
j.write(json.dumps(data,indent=4, ensure_ascii=False))
j.close()

print ("end of script")

