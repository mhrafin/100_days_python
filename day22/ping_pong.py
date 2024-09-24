from turtle import Screen
import bar


def main():
    # - It needs a rectangle black screen.
    screen = Screen()
    screen.bgcolor("black")
    screen.title("Ping Pong Ghor")
    screen.setup(width=1280, height=720, startx=1, starty=1)
    screen.tracer(n=0, delay=1)

    # - There will be a bar class inheriting turtle module.
    player_one = bar.Bar(1)
    player_Two = bar.Bar(2)
    screen.update()
    #     - From that class we will have a two objects of bar one on left and right.
    #     - make bar move with w and s.
    # - There will a ball class which will inherit turtle module.
    # - keep track of score for each player and display it. Maybe make score class?
    screen.exitonclick()
    pass


if __name__ == "__main__":
    main()
