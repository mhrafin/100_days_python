import time
from turtle import Screen

from egg_manager import Egg
from scoreboard_manager import Scoreboard
from snake_manager import Snake

snake = Snake()


def main():
    # Screen Setup
    my_screen = Screen()
    my_screen.title("Snaki Snaki")
    my_screen.setup(width=600, height=600, startx=1, starty=1)
    my_screen.bgcolor("black")
    my_screen.tracer(n=0, delay=1)
    my_screen.listen()

    # Creates an Egg
    egg = Egg()

    # Creates a scoreboard
    scoreboard = Scoreboard()

    # Main game loop
    game_on = True
    snake_moving = True
    egg_spawned = True
    scoreboard_on = False
    while game_on:
        # Updates the Scoreboard
        if not scoreboard_on:
            scoreboard.clear()
            scoreboard.write(
                f"SCORE {scoreboard.score} | High Score {scoreboard.high_score}",
                False,
                align="center",
                font=("Courier", 16, "normal"),
            )
            scoreboard_on = True

        # Snake moving until failure or exit
        if snake_moving:
            my_screen.update()
            time.sleep(0.1)

            snake.move_snake()
            my_screen.onkeypress(fun=snake.turn_up, key="w")
            my_screen.onkeypress(fun=snake.turn_down, key="s")
            my_screen.onkeypress(fun=snake.turn_left, key="a")
            my_screen.onkeypress(fun=snake.turn_right, key="d")
            distance_between = snake.snake_head.distance(egg)
            # print(distance_between)

        if not egg_spawned:
            egg.spawn_an_egg()
            egg_spawned = True
            continue

        # Detect collision with the egg
        if distance_between < 15:
            scoreboard.score += 1
            scoreboard_on = False
            egg_spawned = False
            snake.make_a_snake_part()

        # Detect collision with the walls
        if (
            snake.snake_head.xcor() > 280.0
            or snake.snake_head.xcor() < -280.0
            or snake.snake_head.ycor() > 280.0
            or snake.snake_head.ycor() < -280.0
        ):
            # # print("WALL!!!!!!!!!!")
            # scoreboard.goto(0, 0)
            # scoreboard.write(
            #     "GAME OVER", False, align="center", font=("Courier", 16, "normal")
            # )
            # game_on = False
            # snake.snake_head.goto(0, 0)
            snake.reset_snake()
            scoreboard.record_highscore()
            scoreboard_on = False

        # Detect collision with tail
        for part in snake.snake_parts[1:]:
            distance_from_part = snake.snake_head.distance(part)
            # print(f"snake head: {snake.snake_head.position()}")
            # print(f"part: {part.position()}")
            # print(distance_from_part)
            if distance_from_part < 10:
                # # print("TAIL!!!!!!!!!!")
                # scoreboard.goto(0, 0)
                # scoreboard.write(
                #     "GAME OVER", False, align="center", font=("Courier", 16, "normal")
                # )
                # game_on = False
                snake.reset_snake()
                scoreboard.record_highscore()
                scoreboard_on = False
                break

    # Exits on Click
    my_screen.exitonclick()


if __name__ == "__main__":
    main()
