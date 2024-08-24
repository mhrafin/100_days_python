from gavel_ascii import *
import os

print(logo)
print("Welcome to the secret auction program.")

other_bidders = True

biddings = []

# Adds a bid dict with name and amount to the biddings list
def bid():
    name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: "))
    instance = {
        "bidder_name": name,
        "bidded_amount" : bid_amount
    }
    biddings.append(instance)
    
while other_bidders:
    bid()
    bidders_remain = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if bidders_remain == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    else:
        other_bidders = False
        os.system('cls' if os.name == 'nt' else 'clear')

while not other_bidders:
    max_bid = 0
    max_bidder = ""
    for each in biddings:
        if each["bidded_amount"] > max_bid:
            max_bid = each["bidded_amount"]
            max_bidder = each["bidder_name"]
    
    print(f"The winner is {max_bidder} with a bid of ${max_bid}.")
    break