import colorgram
import turtle
import random


def jpg_to_colorgram_rgb(path_to_jpg: str, num_of_colors: int):
    """Returns a list of rgb colors each a tuple."""
    colors = colorgram.extract(path_to_jpg, num_of_colors)
    rgb_colors = []

    for color in colors:
        rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
    return rgb_colors


colors = jpg_to_colorgram_rgb("./day18/damien-hirst-severed-spots.jpg", 50)


cursor = turtle.Turtle()

active_window = turtle.Screen()
active_window.colormode(255)
active_window.setup(startx=1, starty=1)

cursor.penup()

xaxis = -100
yaxis = -100
cursor.goto(xaxis, yaxis)

for _ in range(10):
    for __ in range(10):
        current_color = random.choice(colors)
        cursor.dot(20, current_color)
        cursor.fd(50)
    yaxis += 50
    cursor.goto(xaxis, yaxis)

cursor.hideturtle()


active_window.exitonclick()
