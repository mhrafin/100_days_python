import os
import random
import sys

def main():
    logo()
    print("Welcome to the Number Guessing Game!")

    while True:
        computers_guess = guess_a_number()
        print("I'm thinking of a number from 1 to 100.")
        
        difficulty = set_difficulty()
        while difficulty != 0:
            print(f"You have {difficulty} attempts to guess the number.")
            players_guess = int(input("Make a guess: "))
            difficulty -= check_guess(players_guess,computers_guess)
        if difficulty == 0:
            print(f"You've run out of guesses, you lose. It was {computers_guess}.")
            play_again()


def logo():
    os.system("cls" if os.name == "nt" else "clear")
    print(r'''
 _______  __   __  _______  _______  _______    _______  __   __  _______    __    _  __   __  __   __  _______  _______  ______   
|       ||  | |  ||       ||       ||       |  |       ||  | |  ||       |  |  |  | ||  | |  ||  |_|  ||  _    ||       ||    _ |  
|    ___||  | |  ||    ___||  _____||  _____|  |_     _||  |_|  ||    ___|  |   |_| ||  | |  ||       || |_|   ||    ___||   | ||  
|   | __ |  |_|  ||   |___ | |_____ | |_____     |   |  |       ||   |___   |       ||  |_|  ||       ||       ||   |___ |   |_||_ 
|   ||  ||       ||    ___||_____  ||_____  |    |   |  |       ||    ___|  |  _    ||       ||       ||  _   | |    ___||    __  |
|   |_| ||       ||   |___  _____| | _____| |    |   |  |   _   ||   |___   | | |   ||       || ||_|| || |_|   ||   |___ |   |  | |
|_______||_______||_______||_______||_______|    |___|  |__| |__||_______|  |_|  |__||_______||_|   |_||_______||_______||___|  |_|
''')
    
def guess_a_number():
    number = random.randint(1,100)
    return number

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "hard":
        return 5
    elif difficulty == "easy":
        return 10
    else:
        return 10
    
def check_guess(player,computer):
    if player == computer:
        logo()
        print(f"Your Guess was {player}.")
        print(f"You got it! The answer was {computer}.")
        play_again()
    elif player > computer:
        logo()
        print(f"Your Guess was {player}.")
        print("It's Too High\nGuess Again.")
        return 1
    elif player < computer:
        logo()
        print(f"Your Guess was {player}.")
        print("It's Too Low\nGuess Again.")
        return 1
    
def play_again():
    play_again = input("Play Again? 'y' or 'n' \n")
    if play_again == 'y':
        main()
    else:
        sys.exit(0)

main()