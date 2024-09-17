from turtle import Turtle
import random


class Egg(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.spawn_an_egg()

    def spawn_an_egg(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)

        self.goto(random_x, random_y)
