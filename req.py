import requests
import json

req = requests.get('https://newapi-6ckm.onrender.com/api').text

js = (json.loads(req))
print()