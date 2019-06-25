import re
import mysql_data 
from dict_assembly import assembleDicts 
import json
from pymongo import MongoClient



def insertDBOne(doc, db):
	try:
		
		if doc['key_word']:
		#print(doc['key_word'])
			volumnName = 'vol_' +  doc['key_word'][:1].lower()
			#print (volumnName)
			collection = db[volumnName]
			objid = collection.insert_one(doc).inserted_id
			
	except Exception as e:
		print('Error: ', e)




#print(sentences)
def writeToMongo(bookInfo, wordList, sentences, db):
	#print(bookInfo, myWord, mySentence)
	
	for word in wordList:
		myWord = word['key_word']
		#print(myWord)
		for sentence in sentences:
			mySentence = sentence['sent_content']
			#print(mySentence)
			pattern = re.compile(r'\b%s\b' % myWord, re.I)
			matchObj = pattern.search(mySentence)
			if (matchObj):
				print(matchObj)
				myDoc =  assembleDicts([bookInfo, word, sentence])
				insertDBOne(myDoc, db)

				
	


BOOK_ID = 4

bookInfo = mysql_data.getBookData(BOOK_ID)

wordList = mysql_data.getWordList(BOOK_ID)

sentences = mysql_data.getSentences(BOOK_ID)

client = MongoClient('localhost', 27017)

DB_NAME = 'lexicon'

db = client[DB_NAME]

writeToMongo(bookInfo, wordList, sentences, db)