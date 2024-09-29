from turtle import Turtle


class Bar:
    def __init__(self, player_no=1 or 2) -> None:
        self.player_one, self.player_two = False, False
        if player_no == 1:
            self.player_one = True
        elif player_no == 2:
            self.player_two = True
        self.make_bar()
        self.max_y_pos = 330
        self.max_y_neg = -330
        pass

    def make_bar(self):
        self.bar = Turtle()
        y_pos = 0
        if self.player_one:
            x_pos = -575
            self.bar.goto(x_pos, y_pos)
        else:
            x_pos = 575
            self.bar.goto(x_pos, y_pos)

        self.bar.penup()
        self.bar.color("white")
        self.bar.shape("square")
        self.bar.resizemode("user")
        self.bar.shapesize(stretch_len=5, stretch_wid=1)
        self.bar.setheading(90)

    def move_up(self):
        if self.max_y_pos > self.bar.ycor():
            self.bar.setheading(90)
            self.bar.forward(30)

    def move_down(self):
        if self.max_y_neg < self.bar.ycor():
            self.bar.setheading(270)
            self.bar.forward(30)
