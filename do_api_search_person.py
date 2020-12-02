import json
import requests
import os
from decouple import config

API_KEY = config('API_KEY')

url = 'https://api.themoviedb.org/3/search/person'
params = dict(
    api_key=API_KEY,
    query='Ryan Gosling',
    page=1
)

resp = requests.get(url=url, params=params)
data = resp.json()
print(data['results'][0]['known_for'][0])