import smtplib
import requests
import datetime as dt
import time
import os

SOFIA = {
    'lat': 42.391554,
    'lng': 25.139835,
    'tzid': 'Europe/Sofia',
    'formatted': 0,
}

MY_EMAIL = os.getenv("MY_GMAIL")
EMAIL_PASS = os.getenv("MY_GMAIL_KEY")
OPEN_WEATHER_KEY = os.getenv("OPEN_WEATHER_KEY")

print(f"Using API Key: {OPEN_WEATHER_KEY}")
print(f"Using EMAIL: {MY_EMAIL}")

PARAMS = {
    'lat': 42.39,
    'lon': 25.13,
    'appid': OPEN_WEATHER_KEY,
    'units': 'metric',
    'cnt': 4
}

OPEN_WEATHER_URL = 'https://api.openweathermap.org/data/2.5/forecast'


def send_mail(message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PASS)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:ISS Is Overhead\n\n"
                                f"{message}"
                            )


weather_response = requests.get(url=OPEN_WEATHER_URL, params=PARAMS)
weather_response.raise_for_status()
weather_response = weather_response.json()

is_clear = False

for hour in weather_response['list']:
    code = int(hour['weather'][0]['id'])
    if 800 <= code <= 802:
        is_clear = True

sun_response = requests.get(url='https://api.sunrise-sunset.org/json', params=SOFIA)
sun_response.raise_for_status()
sun_data = sun_response.json()
sunrise = int(sun_data["results"]["sunrise"].split('T')[1].split(':')[0])
sunset = int(sun_data["results"]["sunset"].split('T')[1].split(':')[0])

tim_now = dt.datetime.now().hour


def is_night():
    if sunset + 1 <= tim_now <= sunrise + 1:
        return True


def is_iss_near():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()

    iss_lng = float(data["iss_position"]['longitude'])
    iss_lat = float(data["iss_position"]['latitude'])

    if (SOFIA['lng'] - 5 <= iss_lng <= SOFIA['lng'] + 5) and \
            (SOFIA['lat'] - 5 <= iss_lat <= SOFIA['lat'] + 5) and is_clear:
        send_mail(f'ISS is at lat{iss_lat}; lng{iss_lng}')


while True:
    is_iss_near()
    time.sleep(180)
