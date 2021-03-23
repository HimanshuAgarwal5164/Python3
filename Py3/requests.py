import requests
import json

page=requests.get('https://api.datamuse.com/words?rel_rhy=funny')
print(type(page))
print('-----------------------------------------------------------------')
print(page.text)
print('-----------------------------------------------------------------')
print(page.url)
print('-----------------------------------------------------------------')
x = page.json()
print(x[0])
print('-----------------------------------------------------------------')
print(json.dumps(x,indent=2))
