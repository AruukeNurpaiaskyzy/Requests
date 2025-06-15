import requests 
from apikey import API_TOKEN

params = {"q" : "Osh", "appid": API_TOKEN, "units": "metric"}


response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
# print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.text)
print(response.json())
