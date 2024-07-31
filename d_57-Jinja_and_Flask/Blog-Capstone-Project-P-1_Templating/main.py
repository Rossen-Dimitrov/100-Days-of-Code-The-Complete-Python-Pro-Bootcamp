import requests
from flask import Flask, render_template
from post import Post

app = Flask(__name__)


blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
response = requests.get(blog_url)
response.raise_for_status()
all_posts = response.json()
obj_list = []
for post in all_posts:
    post_obj = Post(id=post['id'], title=post['title'], subtitle=post['subtitle'], body=post['body'])
    obj_list.append(post_obj)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:post_id>')
def get_post(post_id):
    for obj in obj_list:
        if obj.id == post_id:
            cur_post = obj
    return render_template("post.html", post=cur_post)


if __name__ == "__main__":
    app.run(debug=True)
