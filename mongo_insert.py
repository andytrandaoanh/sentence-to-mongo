import datetime
import json
from pymongo import MongoClient
from pprint import pprint







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
	
myDoc = {'book_id': 1, 'book_title': 'The First-Time Manager', 'book_author': 'Loren B. Belke', 'book_year': 2012, 'key_word': 'abbreviations', 'sent_content': 'Much of the writing in those modalities is choppy and filled with incomplete sentences and abbreviations.', 'sent_num': 3459}

client = MongoClient('localhost', 27017)


DB_NAME = 'lexicon'

db = client[DB_NAME]

insertDBOne(myDoc, db)
