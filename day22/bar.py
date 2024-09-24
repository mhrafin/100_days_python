from turtle import Turtle


class Bar:
    def __init__(self, player_no) -> None:
        if player_no == 1:
            self.player_one = True
            self.player_two = False
        elif player_no == 2:
            self.player_one = False
            self.player_two = True
        self.make_bar()
        pass

    def make_bar(self):
        bar_parts = []
        if self.player_one:
            x_pos = -600
        else:
            x_pos = 600
        y_pos = 0
        for _ in range(4):
            a_turtle = Turtle()
            a_turtle.penup()
            a_turtle.color("white")
            a_turtle.shape("square")
            a_turtle.goto(x_pos, y_pos)
            y_pos -= 20
            bar_parts.append(a_turtle)
