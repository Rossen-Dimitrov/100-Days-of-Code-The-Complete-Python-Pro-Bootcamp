import smtplib
import requests
import datetime as dt
import time

MY_EMAIL = 'xxxxxxx@gmail.com'


def send_mail(email_address, message):
    my_email = MY_EMAIL
    password = "xxxxxxxxx"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email_address,
                            msg=f"Subject:ISS Is Overhead\n\n"
                                f"{message}"
                            )


SOFIA = {
    'lat': 42.391554,
    'lng': 25.139835,
    'tzid': 'Europe/Sofia',
    'formatted': 0,
}

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
            (SOFIA['lat'] - 5 <= iss_lat <= SOFIA['lat'] + 5):
        send_mail(MY_EMAIL, f'ISS is at lat{iss_lat}; lng{iss_lng}')
        print("Mail Sent")


while True:
    is_iss_near()
    time.sleep(180)
