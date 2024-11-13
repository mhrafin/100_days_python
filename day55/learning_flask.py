# # from flask import Flask

# # app = Flask(__name__)


# # def make_bold(function):
# #     def wrapper():
# #         text = function()
# #         return f"<b>{text}</b>"

# #     return wrapper


# # def make_italic(function):
# #     def wrapper():
# #         text = function()
# #         return f"<em>{text}</em>"

# #     return wrapper


# # def make_underlined(function):
# #     def wrapper():
# #         text = function()
# #         return f"<u>{text}</u>"

# #     return wrapper


# # @app.route("/")
# # @make_bold
# # @make_italic
# # @make_underlined
# # def hello():
# #     return "aio hello world"


# # @app.route("/<name>")
# # def home(name):
# #     return f"Hello {name}"


# # if __name__ == "__main__":
# #     app.run(debug=True)


# class User:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.is_logged_in = False


# def is_authenticated_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in:
#             function(args[0])

#     return wrapper


# @is_authenticated_decorator
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post.")


# new_user = User("raf")
# new_user.is_logged_in = True
# create_blog_post(new_user)


def logging_decorator(function):
    def wrapper():
        print(function.__name__)

    return wrapper


@logging_decorator
def my_ass():
    pass


my_ass()
