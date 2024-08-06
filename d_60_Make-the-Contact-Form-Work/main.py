import smtplib

from flask import Flask, render_template, request
import requests
import os

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


def send_mail(email_address, message):
    my_email = os.environ['MY_GMAIL']
    password = os.environ['MY_GMAIL_KEY']

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email_address,
                            msg=message
                            )


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        message = request.form['message']

        message_to_send = (f"Subject:Message from: {name}\n\n"
                           f"Phone: {phone}, Email: {email}"
                           f"Message: {message}")

        send_mail(email, message_to_send)

        return "<h1>Message send successfully!</h1>"

    else:
        return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
