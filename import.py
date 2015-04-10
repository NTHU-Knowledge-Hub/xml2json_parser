'''
Project : K-HUB (XML-Parser)
Date: 2015-10-04
'''

import xml.etree.ElementTree as ET
import csv

#get the details of book
def getBookDetails(book):
	line = []
	for details in book:
		print (details.tag, end=":  ")
		item = book.find(details.tag).text
		#line.append(str(item).replace('\n',' ').replace('\t', ' '))
		print (item)
	#f.writerow(['\t'.join(line)])

#get BookAttributes
def getBookAttributes(book):
	line = []
	for details in book:
		line.append(str(details.tag))
	f.writerow(['\t'.join(line)])


#get the data for each book
def getBooks(itemName):
	#count = 0

	for book in root.iter(itemName):
		#if count == 0:
		#	getBookAttributes(book)
		
		#get the details of the book
		getBookDetails(book)
		#count+=1	

#MAIN######################################################
#f = csv.writer(open("thesis.csv",'a'),delimiter="\t")

#parse the XML file
tree = ET.parse('99.xml')

#obtain root
root = tree.getroot()

#calling to get all books
getBooks ('book')




