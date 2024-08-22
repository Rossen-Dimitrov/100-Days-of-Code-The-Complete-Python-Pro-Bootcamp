from flask import Flask, render_template
import requests
import datetime

date = datetime.datetime.now()
cur_year = date.year

app = Flask(__name__)

API_URL = 'https://api.npoint.io/674f5423f73deab1e9a7'

response = requests.get(API_URL)
response.raise_for_status()

all_posts = [post for post in response.json()]


@app.route("/")
def index():
    return render_template('index.html', posts=all_posts, author='Ross Dim', cur_year=cur_year)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/post/<int:pk>")
def get_post(pk):
    for cur_post in all_posts:
        if cur_post['id'] == pk:
            return render_template('post.html', post=cur_post)

    return "File Not Found"


if __name__ == "__main__":
    app.run(debug=True)
