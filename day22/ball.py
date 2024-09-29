from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.game_over = False
        self.p1_score = 0
        self.p2_score = 0
        self.ball_speed = 2.5

        # print(self.heading())
        # self.setheading(315)
        # print(self.heading())

    def move_ball(self):
        self.forward(self.ball_speed)
        # print(self.ball_speed)
        # print(self.game_over)
        # print(self.xcor())

        if self.ycor() > 350 or self.ycor() < -350:
            self.up_down_wall()

    def up_down_wall(self):
        heading = self.heading()
        now_head_to = 360 - heading
        self.setheading(now_head_to)
        self.ball_speed *= 1.01

    def left_right_wall(self):
        self.game_over = True

    def bounce_off_bar(self, angle=0):
        # print(self.heading())
        self.setheading(angle)
        # print(self.heading())
        self.ball_speed *= 1.02
