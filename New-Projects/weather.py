import requests
from pprint import pprint

API_key = 'c81e448a9297dd385a468b3d554cd6b5'
city = input('Enter a city: ')

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
