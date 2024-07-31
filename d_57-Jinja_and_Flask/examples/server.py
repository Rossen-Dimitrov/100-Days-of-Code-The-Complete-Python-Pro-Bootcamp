from datetime import datetime
import requests

from flask import Flask, render_template

app = Flask(__name__)

AGIFY_URL = 'https://api.agify.io?name='
GENDERIZE_URL = 'https://api.genderize.io?name='


def get_age(name):
    response = requests.get(AGIFY_URL + name)
    response.raise_for_status()
    response = response.json()
    return response['age']


def get_gender(name):
    response = requests.get(GENDERIZE_URL + name)
    response.raise_for_status()
    response = response.json()
    return response['gender']


@app.route('/')
def index():
    year = datetime.now().year
    return render_template('index.html', cur_year=year)


@app.route('/guess/<string:name>')
def guess(name):
    age = get_age(name)
    gender = get_gender(name)
    return render_template('guess.html', age=age, gender=gender, name=name)


@app.route('/blog/<num>')
def get_blog(num):
    print(f'Passed from index page to get_blog function:{num}')
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    response.raise_for_status()
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)
