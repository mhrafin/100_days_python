import csv

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TimeField, URLField
from wtforms.validators import URL, DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
bootstrap = Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location = URLField("Location URL", validators=[DataRequired(), URL()])
    open_time = TimeField("Open Time", validators=[DataRequired()])
    close_time = TimeField("Closing Time", validators=[DataRequired()])
    coffee_rating = SelectField(
        "Coffee Rating",
        choices=["☕️", "☕️☕️", "☕️☕️☕️", "✘"],
        validators=[DataRequired()],
    )
    wifi_rating = SelectField(
        "WiFi Rating",
        choices=["💪", "💪💪", "💪💪💪", "✘"],
        validators=[DataRequired()],
    )
    power_outlets = SelectField(
        "No. of Power Outlets",
        choices=["🔌", "🔌🔌", "🔌🔌🔌", "✘"],
        validators=[DataRequired()],
    )
    submit = SubmitField("Submit")


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")

        new_row = [
            str(form.cafe.data) + ",",
            str(form.location.data) + ",",
            str(form.open_time.data) + ",",
            str(form.close_time.data) + ",",
            str(form.coffee_rating.data) + ",",
            str(form.wifi_rating.data) + ",",
            str(form.power_outlets.data),
        ]

        with open("day62/cafe-data.csv", mode="a") as file:
            file.write("\n")
            for item in new_row:
                file.write(item)

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()

    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open("day62/cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        print(csv_data)
        list_of_rows = []
        for row in csv_data:
            print(row)
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
