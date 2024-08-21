from random import choice
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

KEY = "TopSecretAPIKey"

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # # Method 2. Alternatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=['POST'])
def add_cafe():
    api_key = request.args.get("api-key")
    if api_key == KEY:
        if request.method == 'POST':
            cafe = Cafe(
                name=request.form.get("name"),
                map_url=request.form.get("map_url"),
                img_url=request.form.get("img_url"),
                location=request.form.get("loc"),
                has_sockets=bool(request.form.get("sockets")),
                has_toilet=bool(request.form.get("toilet")),
                has_wifi=bool(request.form.get("wifi")),
                can_take_calls=bool(request.form.get("calls")),
                seats=request.form.get("seats"),
                coffee_price=f'£{request.form.get("coffee_price")}',
            )
            db.session.add(cafe)
            db.session.commit()

            return jsonify(response={"success": f"Successfully added {cafe.name}"}), 200

    else:
        return jsonify({"error": f"Sorry, you don't have permission {api_key}"}), 403


@app.route("/update-price/<cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == KEY:
        cafe = db.get_or_404(Cafe, cafe_id)
        if cafe and request.method == 'PATCH':
            cafe.coffee_price = f'£{request.form.get("new_price")}'
            db.session.commit()

            return jsonify(response={"success": f"Successfully updated {cafe.name}"}), 200

        else:
            return jsonify(error={"Not Found": f"Sorry no cafe with ID: {cafe_id}"}), 404
    else:
        return jsonify({"error": "Sorry, you don't have permission"}), 403


@app.route("/all")
def get_all_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()

    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search")
def search_cafe_by_location():
    location = request.args.get('loc')
    cafe = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalar()
    if cafe:
        return jsonify(cafe=cafe.to_dict())

    return jsonify(error={"Not Found": "Sorry we don't have cafe at that location"}), 404


@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = choice(all_cafes)
    # Simply convert the random_cafe data record to a dictionary of key-value pairs.
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/report-closed/<cafe_id>", methods=['DELETE'])
def delete_cafe(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    api_key = request.args.get("api-key")
    if cafe:
        if api_key == KEY:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": f"Successfully deleted {cafe.name}"}), 200
        else:
            return jsonify({"error": f"Sorry, you don't have permission"}), 403
    else:
        return jsonify(error={"Not Found": f"Sorry no cafe with ID: {cafe_id}"}), 404


# @app.route("/random")
# def random_cafe():
#     random_cafe = choice(Cafe.query.all())
#     return jsonify(cafe={
#         "id": random_cafe.id,
#         "name": random_cafe.name,
#         "map_url": random_cafe.map_url,
#         "img_url": random_cafe.img_url,
#         "location": random_cafe.location,
#         "seats": random_cafe.seats,
#         "has_toilet": random_cafe.has_toilet,
#         "has_wifi": random_cafe.has_wifi,
#         "has_sockets": random_cafe.has_sockets,
#         "can_take_calls": random_cafe.can_take_calls,
#         "coffee_price": random_cafe.coffee_price,
#     })


# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
