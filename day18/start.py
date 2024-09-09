from turtle import Turtle, Screen, done
import random

my_little_turtle = Turtle()
my_screen = Screen()
my_screen.setup(0.5, 0.9, 1, 1)
my_screen.colormode(255)
# my_screen.screensize(500, 500)

# # Creates a square
# my_little_turtle.fd(200)
# my_little_turtle.right(90)
# my_little_turtle.fd(200)
# my_little_turtle.right(90)
# my_little_turtle.fd(200)
# my_little_turtle.right(90)
# my_little_turtle.fd(200)
# my_little_turtle.right(90)

# # Creates a dashed line
# for i in range(50):
#     my_little_turtle.fd(10)
#     my_little_turtle.penup()
#     my_little_turtle.fd(10)
#     my_little_turtle.pendown()

# # Create a lots of shapes starting from triangle
# total_angle = 360
# my_little_turtle.penup()
# my_little_turtle.goto(x=0, y=450)
# my_little_turtle.pendown()
# sides = 3
# for _ in range(3, 11):
#     for i in range(sides):
#         my_little_turtle.forward(100)
#         my_little_turtle.right(total_angle / sides)
#     sides += 1


def random_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# # Creates a random walk
# directions = [0, 90, 180, 270]
# my_little_turtle.pensize(10)
# for _ in range(200):
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     my_little_turtle.pencolor(random_rgb())
#     current_dir = random.choice(directions)
#     my_little_turtle.setheading(current_dir)
#     my_little_turtle.forward(30)

# # Creates a spirograph
# my_little_turtle.speed("fastest")
# angle = 0
# while angle <= 360:
#     my_little_turtle.pencolor(random_rgb())
#     my_little_turtle.circle(100)
#     angle += 4
#     my_little_turtle.setheading(angle)

my_screen.exitonclick()
