import random
import time
from turtle import Screen

import bar
from ball import Ball
from scoreboard import Scoreboard


def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.title("Ping Pong Ghor")
    screen.setup(width=1200, height=800, startx=1, starty=1)
    screen.tracer(n=0, delay=1)
    screen.listen()

    player_one = bar.Bar(1)
    player_two = bar.Bar(2)

    ball = Ball()

    the_scoreboard = Scoreboard()
    the_scoreboard.write(
        f"P1 {ball.p1_score} | {ball.p2_score} P2",
        False,
        align="center",
        font=("Courier", 16, "normal"),
    )

    the_scoreboard.status = False
    global game_on
    game_on = True

    def game_over():
        the_scoreboard.goto(0, 0)
        the_scoreboard.write(
            "GAME OVER!",
            False,
            align="center",
            font=("Courier", 16, "normal"),
        )
        global game_on
        game_on = False

    screen.onkeypress(fun=player_one.move_up, key="w")
    screen.onkeypress(fun=player_one.move_down, key="s")
    screen.onkeypress(fun=player_two.move_up, key="Up")
    screen.onkeypress(fun=player_two.move_down, key="Down")
    screen.onkeypress(fun=game_over, key="x")

    while game_on is True:
        time.sleep(0.01)
        screen.update()
        if not the_scoreboard.status:
            the_scoreboard.clear()
            the_scoreboard.write(
                f"{ball.p1_score} | {ball.p2_score}",
                False,
                align="center",
                font=("Courier", 28, "normal"),
            )
            the_scoreboard.status = True
            screen.update()

        ball.move_ball()

        if player_one.bar.distance(ball) < 50 and ball.xcor() < -560:
            # print(f"p1 to ball = {player_one.bar.distance(ball)}")
            if ball.heading() < 160 and ball.heading() > 90:
                angle = ball.heading() - 90
            elif ball.heading() > 200 and ball.heading() < 270:
                angle = ball.heading() + 90
            else:
                angle = random.choice([21, 19, 341, 339])
            ball.bounce_off_bar(angle)
            ball.forward(10)
            # ball.p1_score += 1
            the_scoreboard.status = False

        elif player_two.bar.distance(ball) < 50 and ball.xcor() > 560:
            # print(f"p2 to ball = {player_two.bar.distance(ball)}")
            if ball.heading() > 20 and ball.heading() < 90:
                # print(1)
                angle = ball.heading() + 90
            elif ball.heading() < 340 and ball.heading() > 270:
                # print(2)
                angle = ball.heading() - 90
            else:
                # print(3)
                angle = random.choice([159, 161, 199, 201])
            # print(f"angle {angle}")
            ball.bounce_off_bar(angle)
            ball.forward(10)
            # ball.p1_score += 1
            the_scoreboard.status = False

        if ball.xcor() > 580:
            # print(ball.xcor())
            ball.p1_score += 1
            the_scoreboard.status = False
            ball.goto(0, 0)
            ball.ball_speed = 2.5
            ball.setheading(random.choice(range(0, 361, 65)))
        elif ball.xcor() < -580:
            # print(ball.xcor())
            ball.p2_score += 1
            the_scoreboard.status = False
            ball.goto(0, 0)
            ball.ball_speed = 2.5
            ball.setheading(random.choice(range(0, 361, 65)))

    screen.exitonclick()


if __name__ == "__main__":
    main()
