from sys import exit
from os import system, name

WATER = 300.0
MILK = 200.0
COFFEE = 100.0

required_ingredients = [
    {"flavor": "espresso", "water": 50, "milk": 0, "coffee": 18, "price": 1.5},
    {"flavor": "latte", "water": 200, "milk": 150, "coffee": 24, "price": 2.5},
    {"flavor": "cappuccino", "water": 250, "milk": 100, "coffee": 24, "price": 3},
]


def main():
    while True:
        print("""
╔═╗┌─┐┌─┐┌─┐┌─┐┌─┐ 
║  │ │├┤ ├┤ ├┤ ├┤  
╚═╝└─┘└  └  └─┘└─┘ 
╔╦╗┌─┐┌─┐┬ ┬┬┌┐┌┌─┐
║║║├─┤│  ├─┤││││├┤ 
╩ ╩┴ ┴└─┘┴ ┴┴┘└┘└─┘
""")
        take_order()


# Take order > 3 hot flavors espresso, latte, cappuccino if sufficient ingredients are available
def take_order():
    choice = input("What do you want! 'Espresso','Latte','Cappuccino' : ").lower()
    for i in required_ingredients:
        if i["flavor"] == choice:
            if i["water"] <= WATER and i["milk"] <= MILK and i["coffee"] <= COFFEE:
                change = payment(i["price"])
                if change > 0:
                    make_coffee(change, i)
                elif change < 0:
                    system("cls" if name == "nt" else "clear")
                    print("You did not enter sufficient coins!")
                else:
                    make_coffee(0, i)
            else:
                system("cls" if name == "nt" else "clear")
                print(
                    f"We are Sorry. We dont have the ingredients for {choice} right now."
                )

    # should also be able to return a report of ingredients current amount
    if choice == "report":
        system("cls" if name == "nt" else "clear")
        print(f"Water: {WATER}\nMilk: {MILK}\nCoffee: {COFFEE}")
    elif choice == "off":
        system("cls" if name == "nt" else "clear")
        print("Turning off Coffee Machine")
        exit(0)


# Coins operator. Checks if coins entered is sufficient and Returns any change.
def payment(price):
    system("cls" if name == "nt" else "clear")
    print("Make Payment")
    penny = float(input("Penny: ")) / 100
    nickel = float(input("Nickel: ")) / 20
    dime = float(input("Dime: ")) / 10
    quarter = float(input("Quarter: ")) / 4

    total = penny + nickel + dime + quarter
    if total >= price:
        change = total - price
        return change
    else:
        return -1


# Make the coffee and serve it.
def make_coffee(change: float, item):
    system("cls" if name == "nt" else "clear")
    global WATER
    global MILK
    global COFFEE

    WATER -= item["water"]
    MILK -= item["milk"]
    COFFEE -= item["coffee"]

    if change != 0:
        print(f"Here is your change {change}.")

    print(f"Here is your {item['flavor']} flavored coffee.")


if __name__ == "__main__":
    main()
