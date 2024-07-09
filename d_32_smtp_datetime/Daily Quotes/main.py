import smtplib
import datetime as dt


def send_mail(email_address, message):
    my_email = "xxxxxxxxxxx@gmail.com"
    password = "xxxxxxxxxxx"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email_address,
                            msg=f"Subject:Daily Quotes\n\n"
                                f"{message}"
                            )


now = dt.datetime.now()
day_of_week = now.weekday()

with open("quotes.txt") as data:
    quotes = data.readlines()
    quote = quotes.pop()

if day_of_week == 1:
    send_mail('xxxxxxxxxxx@abv.bg', quote)


