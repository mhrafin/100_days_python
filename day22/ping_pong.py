from turtle import Screen
import bar
from ball import Ball
import time


def main():
    # - It needs a rectangle black screen.
    screen = Screen()
    screen.bgcolor("black")
    screen.title("Ping Pong Ghor")
    screen.setup(width=1200, height=800, startx=1, starty=1)
    screen.tracer(n=0, delay=1)
    screen.listen()

    # - There will be a bar class.
    #     - From that class we will have a two objects of bar one on left and right.
    player_one = bar.Bar(1)
    player_two = bar.Bar(2)
    # - There will a ball class which will inherit turtle module.
    ball = Ball()

    game_on = True
    while game_on:
        time.sleep(0.1)
        screen.update()
        #     - make bar move with w and s.
        screen.onkeypress(fun=player_one.move_up, key="w")
        screen.onkeypress(fun=player_one.move_down, key="s")
        screen.onkeypress(fun=player_two.move_up, key="Up")
        screen.onkeypress(fun=player_two.move_down, key="Down")

        #   - move the ball
        ball.move_ball()
        #   - Bounce off up and down wall
        #   - Bounce off bar
        dist_bar_one = player_one.bar.distance(ball)
        print(dist_bar_one)
        dist_bar_two = player_two.bar.distance(ball)
        print(dist_bar_two)

        #   - End Game if touched right or left wall

    # - keep track of score for each player and display it. Maybe make score class?
    screen.exitonclick()
    pass


if __name__ == "__main__":
    main()
