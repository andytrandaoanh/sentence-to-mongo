#dic1 = {'book_id': 1, 'book_title': 'The First-Time Manager', 'book_author': 'Loren B. Belke', 'book_year': 2012} 
#dic2 = {'key_word': 'zone'} 
#dic3= {'sent_content': 'The comfort-zone underachiever is trying to find ‘‘what’s right for me.’’ The jobs CZUs take may be temporary; they’re at a crossroads in a period of reassessment.', 'sent_num': 1128}




def assembleDicts(dicList):
	dic_assemble = {}
	for dic in dicList:
		for key in dic:
			dic_assemble[key] = dic[key]
	return dic_assemble


#asb = assembleDics([dic1, dic2, dic3])

#print(asb)

