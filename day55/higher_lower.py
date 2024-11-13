import random

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h><br/><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


number = random.randint(0, 9)
print(number)


@app.route("/<int:guessed_num>")
def found_it(guessed_num):
    if guessed_num < number:
        return "<h1>Too Low</h1><br/><img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXJsMjhyanJ3cXBzaDc3N3NleXJsOTh1NTRqNWR6cmVmbnFmaHJubyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/W5D9oEAJvOHaE/giphy.gif'>"

    if guessed_num > number:
        return "<h1>Too High</h1><br/><img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzM0Nnhwdmg0dnIwY2x5bno3cmx0NWRleWhuOXBsYnAwb25jdmVvNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/rcjl7ufZzCxuo/giphy.gif'>"

    return "<h1>Found It</h1><br/><img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjQ2bzRtc3BmdDRiMXJrdmJqcGNtZDFsMnV3eWlteDc5djc3M3YwMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CF93EZqOxjdHG/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
