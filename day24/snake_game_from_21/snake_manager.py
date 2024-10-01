from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self) -> None:
        self.snake_parts_count = 3
        self.snake_parts: list[Turtle] = []

        # Create snake head
        a_turtle = Turtle()
        a_turtle.shape("square")
        a_turtle.color("white")
        a_turtle.penup()
        a_turtle.speed("fastest")
        self.snake_parts.append(a_turtle)
        self.snake_head = self.snake_parts[0]

        for _ in range(self.snake_parts_count - 1):
            self.make_a_snake_part()

    def make_a_snake_part(self):
        a_turtle = Turtle()
        a_turtle.shape("square")
        a_turtle.color("white")
        a_turtle.penup()
        a_turtle.speed("fastest")

        last_part_pos = self.snake_parts[-1].pos()
        x = float(last_part_pos[0])
        y = float(last_part_pos[1])
        a_turtle.goto(x, y)

        self.snake_parts.append(a_turtle)

    def move_snake(self):
        new_x = self.snake_head.xcor()
        new_y = self.snake_head.ycor()

        self.snake_head.forward(MOVE_DISTANCE)
        for part in self.snake_parts[1:]:
            old_x = part.xcor()
            old_y = part.ycor()
            part.goto(new_x, new_y)
            new_x = old_x
            new_y = old_y
        self.turn_need = True

    def turn_up(self):
        if self.snake_head.heading() != 270 and self.turn_need:
            self.snake_head.setheading(90)
            # print("up")
            self.turn_need = False

    def turn_down(self):
        if self.snake_head.heading() != 90 and self.turn_need:
            self.snake_head.setheading(270)
            # print("down")
            self.turn_need = False

    def turn_left(self):
        if self.snake_head.heading() != 0 and self.turn_need:
            self.snake_head.setheading(180)
            # print("left")
            self.turn_need = False

    def turn_right(self):
        if self.snake_head.heading() != 180 and self.turn_need:
            self.snake_head.setheading(0)
            # print("right")
            self.turn_need = False

    def reset_snake(self):
        for part in self.snake_parts:
            part.hideturtle()

        # print(self.snake_parts)
        self.snake_parts.clear()
        # print(self.snake_parts)
        a_turtle = Turtle()
        a_turtle.shape("square")
        a_turtle.color("white")
        a_turtle.penup()
        a_turtle.speed("fastest")
        # print(a_turtle.position())
        self.snake_parts.append(a_turtle)
        self.snake_head = self.snake_parts[0]

        for _ in range(self.snake_parts_count - 1):
            self.make_a_snake_part()
            self.move_snake()
