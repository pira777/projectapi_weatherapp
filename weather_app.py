import os
import requests
from datetime import datetime

api_key = os.environ.get('WEATHERAPP_APIKEY')
# print(api_key)

while True:
    location = input('Location: ')

    result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&unit=metric&appid={api_key}')

    if result.json()['cod'] == '404':
        print('Invalid location!')
        continue
    break
# print(result)
# print(result.json())
description = result.json()['weather'][0]['description']

temperature = round(result.json()['main']['temp']-276)

feels_like = round(result.json()['main']['feels_like']-276)

high = round(result.json()['main']['temp_max']-276)

low = round(result.json()['main']['temp_min']-276)

hmdt = result.json()['main']['humidity']

wind_speed = result.json()['wind']['speed']

date_time = datetime.now().strftime('%d %b %Y %I :%M:%S %p')

print(f'======================================')
# print(feels_like)
print(f'The weather in {location} is {temperature}\N{DEGREE CELSIUS}  with {description}')
print(f'It feels like {feels_like}\N{DEGREE CELSIUS}.')
print(f"Today's high\N{DEGREE CELSIUS}  and today's low\N{DEGREE CELSIUS}")
print(f'{location} temperature is {temperature}\N{DEGREE CELSIUS}')
print(f'======================================')

print(f'Current Humidity : {hmdt} %')
print(f'Current Wind Speed : {wind_speed} kmph')