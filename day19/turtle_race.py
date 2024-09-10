import turtle as t
import turtles_setup
import random


def main():
    window = t.Screen()
    window.colormode(255)
    window.setup(500, 400, 1, 1)
    player_guess = window.textinput(
        "Turtle Game",
        "Who do you think will win? \n'red' or 'orange' or 'yellow' or 'green' or 'blue' or 'indigo' or 'violet': ",
    ).lower()
    num_turtles = int(
        window.numinput("Turtle Game", "Number of Turtles", minval=1, maxval=7)
    )
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    turtles = ready_turtles(num_turtles, colors)

    for i, turtle in enumerate(turtles):
        turtle.turtle_object.goto(-230, -i * 30 + 60)

    race_ongoing = True
    while race_ongoing:
        racing(turtles)
        finished = finish_line_crossed(turtles)
        if finished:
            if finished.turtle_object.fillcolor() == player_guess:
                print(f"You Won! {finished.turtle_object.fillcolor()} turtle won!")
            else:
                print(f"You Lost! {finished.turtle_object.fillcolor()} turtle won!")
            break

    window.exitonclick()


def ready_turtles(num_of_turtles, colors):
    turtles = []
    for i in range(num_of_turtles):
        turtles.append(turtles_setup.TurtleSetup(shape="turtle", color=colors[i]))
    return turtles


def racing(turtles: list):
    for turtle in turtles:
        turtle.turtle_object.forward(random.randrange(1, 10) / 5)


def finish_line_crossed(turtles):
    for turtle in turtles:
        if int(turtle.turtle_object.xcor()) == 200:
            # print(turtle.turtle_object.position())
            return turtle
    return False


if __name__ == "__main__":
    main()
