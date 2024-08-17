import random

from hangman_ascii import *
from hangman_words import *

print(hangman_logo)

chosen_word = random.choice(word_list).lower()

progress = []
for each in range(len(chosen_word)):
    progress += "_"

life = 7
while "_" in progress and life != 0:
    # print(("_" in progress and life != 0))
    print(progress)
    guess = input("Guess a letter: ").lower()
    found = 0
    duplicate_entry = 0
    for i in range(len(chosen_word)):
        
        # print(guess)
        # print(i)
        # print(guess == chosen_word[i])
        if guess in progress[i]:
            duplicate_entry += 1
            continue
        if guess == chosen_word[i]:
            progress[i] = guess
            found += 1              

    if guess in progress and duplicate_entry > 0:
        print(f"You already found {guess}")
        continue

    
    if found == 0:

        life -= 1
        print(f"{hangman[life]}")
    #print(f"Life Remaining: {life}")
    

    
if "_" not in progress:
    print("You won!")
else:
    print("You lost!")
