import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
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
        dictionary = {}
        # print(self.__table__)
        # print(self.__table__.c)
        # print(getattr(self.__table__.columns))

        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)

        return dictionary


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def get_random():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all", methods=["GET"])
def get_all():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    to_return_dict = []
    for cafe in all_cafes:
        to_return_dict.append(cafe.to_dict())
    return jsonify(cafes=to_return_dict)


@app.route("/search", methods=["GET"])
def search():
    location = request.args.get("location")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == location))
    all_cafes = result.scalars().all()
    to_return_dict = []
    for cafe in all_cafes:
        to_return_dict.append(cafe.to_dict())
    if all_cafes:
        return jsonify(cafes=to_return_dict)
    else:
        return jsonify(error={"Not Found": "Sorry!"})


# HTTP POST - Create Record
@app.route("/add", methods=["GET", "POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    result = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    if request.method == "PATCH":
        updated_price = request.form.get("updated_price")
        result.coffee_price = updated_price

        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    return jsonify(result={"error": "Sorry!"}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api_key")
    if api_key == "TopSecretAPIKey":
        cafe = db.get_or_404(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(
                response={"success": "Successfully deleted the cafe from the database."}
            ), 200
        else:
            return jsonify(
                error={
                    "Not Found": "Sorry a cafe with that id was not found in the database."
                }
            ), 404
    else:
        return jsonify(
            error={
                "Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."
            }
        ), 403


if __name__ == "__main__":
    app.run(debug=True)


# name:Cozy Corner Cafe2
# map_url:https://goo.gl/maps/xyz123
# img_url:https://example.com/image.jpg
# location:Brewtown
# seats:25
# has_toilet:True
# has_wifi:True
# has_sockets:False
# can_take_calls:True
# coffee_price:$4.50
