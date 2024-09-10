import turtle

cursor = turtle.Turtle()
window = turtle.Screen()
window.setup(1000, 1000, 1, 1)


def move_forward():
    cursor.forward(10)


def move_backward():
    cursor.backward(10)


def turn_left():
    cursor.left(10)


def turn_right():
    cursor.right(10)


def clear_screen():
    cursor.reset()


def exit():
    window.bye()


window.listen()
window.onkeypress(fun=move_forward, key="w")
window.onkeypress(fun=move_backward, key="s")
window.onkeypress(fun=turn_left, key="a")
window.onkeypress(fun=turn_right, key="d")
window.onkeypress(fun=clear_screen, key="c")
window.onkeypress(fun=exit, key="x")


window.exitonclick()
