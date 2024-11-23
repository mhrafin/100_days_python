import os

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    app.root_path, "library.db"
)
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Book).order_by(Book.name))
    all_books = result.scalars()
    # print(all_books.name)
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        one_entry = Book(
            name=request.form.get("name"),
            author=request.form.get("author"),
            rating=request.form.get("rating"),
        )
        db.session.add(one_entry)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/new-rating", methods=["GET", "POST"])
def new_rating():
    # GET
    id = request.args.get("id")
    result = db.session.execute(db.select(Book).where(Book.id == id))
    book = result.scalar()

    # POST
    # Using id to find the book to be updated.
    # Catching the new rating from the form using the input's name.
    if request.method == "POST":
        book_to_be_updated = db.session.execute(
            db.select(Book).where(Book.id == id)
        ).scalar()
        new_rate = float(request.form.get("rating", default=0))
        book_to_be_updated.rating = new_rate
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_rating.html", book=book)


@app.route("/deleted", methods=["GET", "POST"])
def delete_row():
    id = request.args.get("id")
    book_to_be_deleted = db.session.execute(
        db.select(Book).where(Book.id == id)
    ).scalar()
    db.session.delete(book_to_be_deleted)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
