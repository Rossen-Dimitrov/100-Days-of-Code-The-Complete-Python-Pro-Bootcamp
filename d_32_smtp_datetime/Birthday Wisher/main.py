import smtplib
import datetime as dt
import pandas
import random
import os


def send_mail(email_address, message):
    my_email = "xxxxxxxxxxx@gmail.com"
    password = "xxxxxxxxxxx"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email_address,
                            msg=f"Subject:Happy Birthday\n\n"
                                f"{message}"
                            )


b_day_data = pandas.read_csv('birthdays.csv')
b_day = b_day_data.to_dict(orient='records')
now = dt.datetime.now()
today = (now.month, now.day)

for record in b_day:
    date = (record['month'], record['day'])
    if date == today:
        num = random.randint(1, 3)
        with open(f'letter_templates/letter_{num}.txt') as data:
            letter = data.read()
            letter = letter.replace('[NAME]', record['name'])
        send_mail(record['email'], letter)
