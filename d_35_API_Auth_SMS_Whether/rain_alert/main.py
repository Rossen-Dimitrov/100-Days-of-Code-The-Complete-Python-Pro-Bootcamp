import requests

PARAMS = {
    'lat': 42.69,
    'lon': 23.32,
    'appid': "10a8c8d9762dfe36266142aee6d47ca1",
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
