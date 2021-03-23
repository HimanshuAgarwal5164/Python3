import requests
import json
import webbrowser

##  flickr api key - 0b350061f1c7050b09a6ffe0973544ac
##  secret - 7a2b5f024dfd25aa

d={
    'api_key':'0b350061f1c7050b09a6ffe0973544ac',
    'method':'flickr.photos.search',
    'format':'json',
    'tags':'kashmir',
    'nojsoncallback':1,
    'media':'photos',
    'per_page':10
    }


page=requests.get('https://api.flickr.com/services/rest',params=d)
print(page.url)
x=page.json()
y=x['photos']['photo']
for i in y:
    p_id=i['id']
    owner=i['owner']
    url='https://www.flickr.com/photos/{}/{}'.format(owner,p_id)
    print(url)
    webbrowser.open(url)
