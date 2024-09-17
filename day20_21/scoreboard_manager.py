from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
