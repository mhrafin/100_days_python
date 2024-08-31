import random
import textwrap
from os import name, system
from sys import exit

import tv_show_list


def main():
    logo()
    # Need a list of subjects with a metric to compare them
    # Select two of them at Random
    score = 0
    item_a = random.choice(tv_show_list.tv_shows)
    wrapped_description_a = textwrap.fill(item_a["description"])

    item_b = random.choice(tv_show_list.tv_shows)
    wrapped_description_b = textwrap.fill(item_b["description"])

    while item_a["episodes"] == item_b["episodes"]:
        item_b = random.choice(tv_show_list.tv_shows)
        wrapped_description_b = textwrap.fill(item_b["description"])

    while True:
        # Show items and ask
        print(f"Compare A: \n{item_a['name']}, \n{wrapped_description_a}")
        print(r"""
 _    _ _______
  \  /  |______
   \/   ______|
""")
        print(f"Against B: \n{item_b['name']}, \n{wrapped_description_b}\n")
        print("Does B has Higher or Lower no. of episodes than A.")
        ans = input("Type 'Higher' or 'Lower'\n").lower()

        if ans == "higher":
            if item_a["episodes"] > item_b["episodes"]:
                system("cls" if name == "nt" else "clear")

                print("You Lost!")
                print(f"Your Score is {score}.")
                exit(0)
            elif item_a["episodes"] < item_b["episodes"]:
                system("cls" if name == "nt" else "clear")

                print("You Win!")
                item_a = item_b
                while item_a["episodes"] == item_b["episodes"]:
                    item_b = random.choice(tv_show_list.tv_shows)
                    wrapped_description_b = textwrap.fill(item_b["description"])
                score += 1
                print(f"Your Score is {score}.")
                continue
        elif ans == "lower":
            if item_a["episodes"] > item_b["episodes"]:
                system("cls" if name == "nt" else "clear")

                print("You Win")
                item_a = item_b
                while item_a["episodes"] == item_b["episodes"]:
                    item_b = random.choice(tv_show_list.tv_shows)
                    wrapped_description_b = textwrap.fill(item_b["description"])
                score += 1
                print(f"Your Score is {score}.")
                continue
            elif item_a["episodes"] < item_b["episodes"]:
                system("cls" if name == "nt" else "clear")

                print("You Lost!")
                print(f"Your Score is {score}.")
                exit(0)
        else:
            exit(0)


def logo():
    print(r"""
 _     _ _____  ______ _     _ _______  ______
 |_____|   |   |  ____ |_____| |______ |_____/
 |     | __|__ |_____| |     | |______ |    \_
                                              
         _____  _  _  _ _______  ______       
 |      |     | |  |  | |______ |_____/       
 |_____ |_____| |__|__| |______ |    \_       
""")


if __name__ == "__main__":
    main()
