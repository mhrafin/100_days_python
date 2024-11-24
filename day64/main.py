import os
from pprint import pp

import requests
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, session, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import FloatField, IntegerField, StringField, SubmitField
from wtforms.validators import URL, DataRequired

from flask_session import Session

load_dotenv()

API_KEY = os.getenv("TMDB_API")
print(API_KEY)

search_url = "https://api.themoviedb.org/3/search/movie"

headers = {"accept": "application/json", "Authorization": "Bearer " + API_KEY}

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
#     app.root_path, "database.db"
# )
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True, default=0.0)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True, default=0)
    review: Mapped[str] = mapped_column(String, nullable=True, default="")
    img_url: Mapped[str] = mapped_column(String, nullable=False)


with app.app_context():
    db.create_all()


# Edit Form
class EditForm(FlaskForm):
    rating = FloatField("Your rating out 10 e.g 7.5", validators=[DataRequired()])
    # ranking = IntegerField("Your Ranking", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Update")


class AddForm(FlaskForm):
    title = StringField("Name of the Movie", validators=[DataRequired()])
    submit = SubmitField("Search Movie")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars()
    all_movies = result.all()  # convert ScalarResult to Python List

    for i in range(len(all_movies)):
        all_movies[i].ranking = i + 1
    db.session.commit()

    print(all_movies[0].title)

    return render_template("index.html", data=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    id = request.args.get("id")
    result = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
    form = EditForm()

    if form.validate_on_submit():
        result.rating = form.rating.data
        # result.ranking = form.ranking.data
        result.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=result, form=form)


@app.route("/delete")
def delete():
    id = request.args.get("id")
    result = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()

    db.session.delete(result)
    db.session.commit()

    return redirect(url_for("home"))


def get_query_data(query):
    parameters = {"query": query}

    response = requests.get(search_url, headers=headers, params=parameters)

    pp(response.json()["results"])
    return response.json()["results"]


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()

    if form.validate_on_submit():
        query = form.title.data
        return redirect(url_for("select", query=query))

    return render_template("add.html", form=form)


@app.route("/select/<query>")
def select(query):
    data_list = get_query_data(query=query)
    movies = {str(movie["id"]): movie for movie in data_list}
    session["movies"] = movies
    return render_template("select.html", data=data_list)


@app.route("/add_to_db/")
def add_to_db():
    new_id = request.args.get("id")
    movies = session.get("movies")
    movie_data = movies.get(str(new_id))
    pp(movie_data)

    new_movie = Movie(
        title=movie_data["original_title"],
        year=int(movie_data["release_date"][0:4]),
        description=movie_data["overview"],
        img_url="https://image.tmdb.org/t/p/w500" + movie_data["poster_path"],
    )
    db.session.add(new_movie)
    db.session.commit()

    id_ = (
        db.session.execute(
            db.select(Movie).where(Movie.title == movie_data["original_title"])
        )
        .scalar()
        .id
    )
    return redirect(url_for("edit", id=id_))


if __name__ == "__main__":
    app.run(debug=True)
