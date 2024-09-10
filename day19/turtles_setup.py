import turtle


class TurtleSetup:
    def __init__(self, shape: str, color: tuple) -> None:
        self.turtle_object = turtle.Turtle()
        self.turtle_object.shape(shape)
        self.turtle_object.fillcolor(color)
        self.turtle_object.penup()
