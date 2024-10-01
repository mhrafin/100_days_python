from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        with open("day24/snake_game_from_21/data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.penup()
        self.speed("fastest")
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
    
    def record_highscore(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("day24/snake_game_from_21/data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
