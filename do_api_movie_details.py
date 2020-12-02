import json
import requests
import os
from decouple import config

API_KEY = config('API_KEY')
movie= 335984

url = f'https://api.themoviedb.org/3/movie/{movie}'
params = dict(
    api_key=API_KEY,
)

resp = requests.get(url=url, params=params)
data = resp.json()
print(data['original_title'], data['overview'], data['release_date'])