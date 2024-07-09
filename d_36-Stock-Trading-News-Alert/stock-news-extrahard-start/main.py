import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
from datetime import date
from datetime import timedelta

MY_EMAIL = os.getenv("MY_GMAIL")
EMAIL_PASS = os.environ.get("MY_GMAIL_KEY")

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API = "B93SMK2Q639948ZS"
STOCK_PARAMS = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_API,
}
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY = "c9e0f4a06a0d4387a2ada26d9ff70992"
DAYS_BEFORE = 2
NEWS_PARAMS = {
    'q': COMPANY_NAME,
    'from': date.today() - timedelta(days=DAYS_BEFORE),
    'apiKey': NEWS_KEY,
    'searchIn': 'title',
}


def check_prices():
    stock_response = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMS)
    stock_response.raise_for_status()
    stock_data = stock_response.json()['Time Series (Daily)']
    stock_list = [value for (key, value) in stock_data.items()]
    yesterday_data = float(stock_list[0]['4. close'])
    day_before_yesterday_data = float(stock_list[1]['4. close'])
    difference = abs(yesterday_data - day_before_yesterday_data)
    difference_percents = (difference / yesterday_data) * 100
    # print(difference_percents)
    if difference_percents >= 5:
        get_news()


def get_news():
    news_response = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMS)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data['articles'][:3]
    message = ''
    for article in articles:
        message += article['title'] + '\n'
        message += article['description'] + '\n'
        message += article['url'] + '\n'
        message += '#' * 50 + '\n'

    send_mail(message)


def send_mail(message):
    msg = MIMEMultipart()
    msg['From'] = MY_EMAIL
    msg['To'] = MY_EMAIL
    msg['Subject'] = "Last 3 Articles"

    part = MIMEText(message, 'plain', 'utf-8')
    msg.attach(part)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=EMAIL_PASS)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=msg.as_string()
                                )
            print("Email sent successfully.")

    except Exception as e:
        print(f"Failed to send email: {e}")


check_prices()
