from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.game_over = False

        # print(self.heading())
        # self.setheading(315)
        # print(self.heading())

    def move_ball(self):
        self.forward(10)
        # time.sleep(0.1)
        # print(f"(x,y): {self.xcor()},{self.ycor()}")
        if self.ycor() > 350:
            self.up_wall()
        elif self.ycor() < -350:
            self.down_wall()

    def up_wall(self):
        heading = self.heading()
        now_head_to = 270 - (heading - 90)
        self.setheading(now_head_to)

    def down_wall(self):
        heading = self.heading()
        now_head_to = heading - 270
        self.setheading(now_head_to)

    def left_right_wall(self):
        if self.xcor() > 600 or self.xcor() < -600:
            self.game_over = True

    def bounce_off_bar():
        pass
