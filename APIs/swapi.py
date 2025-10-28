import requests
import json

base_url = "https://swapi.dev/api/"
endpoint = "people/5/"

response = requests.get(base_url + endpoint)
data = response.json()
print(data['name'])