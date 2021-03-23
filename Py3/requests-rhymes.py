import requests
import json

a = input('Enter word')
d={}
d['rel_rhy']=a
page = requests.get('https://api.datamuse.com/words',params=d)
x=page.json()
rhymes = [i['word']for i in x]
for i in rhymes:
    print(i)
