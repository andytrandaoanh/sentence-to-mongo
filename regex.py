import re

sentence = 'Two man in the boats'
word = 'boats'

pattern = re.compile(r'\b%s\b' % word, re.I)

matchObj = pattern.search(sentence)

if matchObj:
	print('found')
else:
	print('not able to find')