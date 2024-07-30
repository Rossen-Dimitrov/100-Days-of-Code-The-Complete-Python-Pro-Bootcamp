from random import randint

from flask import Flask

app = Flask(__name__)

random_number = randint(1, 10)


@app.route('/')
def home():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>")


@app.route("/<int:number>")
def gues(number):
    if number > random_number:
        return ('<h2>Try Lower</h2>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
    elif number < random_number:
        return ('<h2>Try Higher</h2>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
    else:
        return ('<h2>You Guessed It</h2>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')


if __name__ == "__main__":
    app.run(debug=True)
