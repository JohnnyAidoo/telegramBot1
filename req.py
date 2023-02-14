import requests
import json

req = requests.get('https://newapi-6ckm.onrender.com/api').text

data = json.loads(req)
head = data[0]['head'] 
One = data[0]['url']