import requests
from requests.auth import HTTPBasicAuth

headers = {'Accept':'application/json; version=v2'}

response = requests.get('http://127.0.0.1:8000/api/authors/',headers=headers)
print(response.json())