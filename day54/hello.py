# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

import time


def this_decorates(a_function):
    def this_is_the_final_decorated_function():
        time.sleep(2)  # Doing something extra that is not part of the a_fucntion
        # Do something before if needed
        a_function()
        a_function()  # We can call the a_function as many times as we want
        # Do something after if needed
        # Mainly this is playground. Here we play with a_function as we like.

    return this_is_the_final_decorated_function


@this_decorates
def a():
    print("I am a function. I would love a 2 sec delay.")


@this_decorates
def b():
    print("I am a function. I would love a 2 sec delay.")


@this_decorates
def c():
    print("I am a function. I would love a 2 sec delay.")
