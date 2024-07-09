import requests
import os

MY_EMAIL = os.getenv("MY_GMAIL")
EMAIL_PASS = os.environ.get("MY_GMAIL_KEY")
OPEN_WEATHER_KEY = os.environ["OPEN_WEATHER_KEY"]


PARAMS = {
    'lat': 42.69,
    'lon': 23.32,
    'appid': OPEN_WEATHER_KEY,
    'units': 'metric',
    'cnt': 4
}
URL = 'https://api.openweathermap.org/data/2.5/forecast'

response = requests.get(url=URL, params=PARAMS)
response.raise_for_status()
response = response.json()


for hour in response['list']:
    code = int(hour['weather'][0]['id'])
    if code >= 800:
        print("It's cloudy")
        break
