from turtle import Screen, Turtle

import pandas


def main():
    screen = Screen()
    screen.title("Us States Game")
    screen.setup(width=800, height=500, startx=1, starty=1)

    image = "day25/us-states-game-start/blank_states_img.gif"
    screen.addshape(image)

    us_map = Turtle()
    us_map.shape(image)

    def get_mouse_click_coor(x, y):
        print(f"Clicked at: ({x}, {y})")

    screen.onscreenclick(get_mouse_click_coor)

    states_data = pandas.read_csv("day25/us-states-game-start/50_states.csv")
    states = states_data.state.tolist()

    state_turtles: dict[str, Turtle] = {}

    guessed_states = []
    while len(guessed_states) < 50:
        player_guess: str = (
            screen.textinput(
                title=f"{len(guessed_states)}/50 Times Guessed", prompt="What's another state name?"
            )
        ).title()
        # print(player_guess)

        if player_guess == "Exit":
            break

        if player_guess in states:
            current_row: pandas.DataFrame = states_data[
                states_data["state"] == player_guess
            ]
            # print(type(current_row.x))
            # print(type(current_row.at[current_row.index[0], "x"]))

            guessed_states.append(player_guess)

            state_name = current_row.at[int(current_row.index[0]), "state"]
            cor_x = current_row.at[int(current_row.index[0]), "x"]
            cor_y = current_row.at[int(current_row.index[0]), "y"]

            state_turtles[state_name] = Turtle()
            state_turtles[state_name].penup()
            state_turtles[state_name].hideturtle()
            state_turtles[state_name].goto(cor_x, cor_y)
            state_turtles[state_name].write(f"{state_name}")

    with open('day25/us-states-game-start/Result.csv', 'w'):
        pass
    with open("day25/us-states-game-start/Result.csv", mode="a") as result_file:
        result_file.write("Your missed states:\n")
        for state in states:
            if state not in guessed_states:
                result_file.write(f"{state}\n")


if __name__ == "__main__":
    main()
