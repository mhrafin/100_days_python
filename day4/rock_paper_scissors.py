import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""

elements = [rock, paper, scissor]

print("Welcome to Rock, Paper & Scissor!")
print("What do you choose? Type 0 for rock, 1 for paper, 2 for scissor")

user_choice = int(input())

pc_choice = random.randint(0,2)

if user_choice == pc_choice:
    print(f"Your choice: {elements[user_choice]}")
    print(f"PC choice: {elements[pc_choice]}")
    print("And its a draw!")

if user_choice == 0 and pc_choice == 1:
    print(f"Your choice: {elements[user_choice]}")
    print(f"PC choice: {elements[pc_choice]}")
    print("PC Wins!")

if user_choice == 0 and pc_choice == 2:
    print(f"Your choice: {elements[user_choice]}")
    print(f"PC choice: {elements[pc_choice]}")
    print("You Win!")

if user_choice == 1 and pc_choice == 0:
    print(f"Your choice: {elements[user_choice]}")
    print(f"PC choice: {elements[pc_choice]}")
    print("You Win!")

if user_choice == 1 and pc_choice == 2:
    print(f"Your choice: {elements[user_choice]}")
    print(f"PC choice: {elements[pc_choice]}")
    print("PC Wins!")

if user_choice == 2 and pc_choice == 0:
    print(f"Your choice: {elements[user_choice]}")
    print(f"PC choice: {elements[pc_choice]}")
    print("PC Wins!")

if user_choice == 2 and pc_choice == 1:
    print(f"Your choice: {elements[user_choice]}")
    print(f"PC choice: {elements[pc_choice]}")
    print("You Win!")