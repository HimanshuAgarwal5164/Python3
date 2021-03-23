import requests
import json

d = {'term':'Adele','media':'music'}
page = requests.get('https://itunes.apple.com/search',params=d)
print(page.url)
x=page.json()
results = x['results']
for result in results:
    print(result['trackName'])
