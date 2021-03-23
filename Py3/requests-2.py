import requests
import json

d={'q':'violins and guitars','tbm':'isch'}
page = requests.get('https://google.com/search',params=d)
print(page.text)
