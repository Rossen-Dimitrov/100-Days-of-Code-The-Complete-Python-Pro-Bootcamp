from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, URLField
from wtforms.validators import DataRequired
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE

class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


class EditMovieForm(FlaskForm):
    ranking = FloatField(label='Ranking', validators=[DataRequired()])
    review = StringField(label='Review', validators=[DataRequired()])
    submit = SubmitField('Update')


class AddMovieForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


# Manual creating movies
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
#
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()


def get_movies(movie):
    movie_db_url = 'https://api.themoviedb.org/3/search/movie'
    movie_db_key = os.environ["MOVIE_DB_KEY"]

    response = requests.get(url=movie_db_url, params={'api_key': movie_db_key, 'query': movie})
    response.raise_for_status()
    data = response.json()['results']
    return data


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.ranking))
    all_movies = result.scalars().all() # convert ScalarResult to Python List

    # all_movies = db.session.execute(db.select(Movie).order_by(Movie.ranking)).scalars()

    return render_template("index.html", all_movies=all_movies)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovieForm(request.form)
    if request.method == 'POST':
        title = request.form['title']
        movies = get_movies(title)
        return render_template('select.html', movies=movies)
    return render_template('add.html', form=form)


@app.route("/find")
def get_movie_details():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_db_url = 'https://api.themoviedb.org/3/movie/' + movie_api_id
        movie_db_key = os.environ["MOVIE_DB_KEY"]

        response = requests.get(url=movie_db_url, params={'api_key': movie_db_key})
        response.raise_for_status()
        data = response.json()

        title = data["title"]
        img_url = "https://image.tmdb.org/t/p/original" + data["poster_path"]
        year = data["release_date"].split('-')[0]
        description = data["overview"]
        rating = data["vote_average"]
        review = "Add my own review"
        img_url = img_url

        new_movie = Movie(
            title=title,
            year=year,
            description=description,
            rating=rating,
            review=review,
            img_url=img_url
        )

        db.session.add(new_movie)
        db.session.commit()

    return redirect(url_for("edit", id=new_movie.id))


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    movie = db.get_or_404(Movie, id)
    form = EditMovieForm(formdata=request.form, obj=movie)
    if form.validate_on_submit():
        if request.method == 'POST' and form.validate():
            movie.ranking = float(form.ranking.data)
            movie.review = form.review.data
            db.session.commit()
            return redirect(url_for("home"))
    return render_template('edit.html', movie=movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
