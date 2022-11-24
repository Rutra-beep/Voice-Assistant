import requests
from ss import *

api__address = 'https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=fcb12e193066b6099661d5fc776d5aa3' 
json_data = requests.get(api__address).json()

def temp():
    temperature = round(json_data["main"]["temp"]-273,1)
    return temperature

def des():
    description = json_data["weather"][0]["description"]
    return description

print(temp())
print(des())