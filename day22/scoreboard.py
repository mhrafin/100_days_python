from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.goto(0, 350)
        self.color("white")
        self.hideturtle()
        self.status = False
