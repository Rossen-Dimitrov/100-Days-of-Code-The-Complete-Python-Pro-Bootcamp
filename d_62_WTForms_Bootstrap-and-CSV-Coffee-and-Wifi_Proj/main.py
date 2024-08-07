from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

COFFE_RATING_CHOICE = [
    ('✘', '✘'),
    ('☕', '☕'),
    ('☕☕', '☕☕'),
    ('☕☕☕', '☕☕☕'),
    ('☕☕☕☕️', '☕☕☕☕️'),
    ('☕☕☕☕☕', '☕☕☕☕☕'),
]

WIFI_RATING_CHOICE = [
    ('✘', '✘'),
    ('💪', '💪'),
    ('💪💪', '💪💪'),
    ('💪💪💪', '💪💪💪'),
    ('💪💪💪💪', '💪💪💪💪'),
    ('💪💪💪💪💪', '💪💪💪💪💪'),
]
POWER_RATING_CHOICE = [
    ('✘', '✘'),
    ('🔌', '🔌'),
    ('🔌🔌', '🔌🔌'),
    ('🔌🔌🔌', '🔌🔌🔌'),
    ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),
    ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'),
]


class CafeForm(FlaskForm):
    cafe_name = StringField(label='Cafe Name', validators=[DataRequired()])
    location_url = StringField(label='Location URL', validators=[DataRequired(), URL()])
    open_time = StringField(label='Open time', validators=[DataRequired()])
    closing_time = StringField(label='Closing time', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee rating', validators=[DataRequired()], choices=COFFE_RATING_CHOICE)
    wifi_rating = SelectField(label='WiFi rating', validators=[DataRequired()], choices=WIFI_RATING_CHOICE)
    power_rating = SelectField(label='Power outlet', validators=[DataRequired()], choices=POWER_RATING_CHOICE)
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if request.method == 'POST' and form.validate_on_submit():
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe_name.data},"
                           f"{form.location_url.data},"
                           f"{form.open_time.data},"
                           f"{form.closing_time.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_rating.data}")
        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
