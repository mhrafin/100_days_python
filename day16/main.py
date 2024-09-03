import os

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


espresso = MenuItem("espresso", 50, 0, 18, 1.5)
latte = MenuItem("latte", 200, 150, 24, 2.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3)

a_menu = Menu()
a_menu.menu = [espresso, latte, cappuccino]
print(a_menu.get_items())

a_coffeemaker = CoffeeMaker()
a_moneymachine = MoneyMachine()


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
        choice = input("What do you want! 'Espresso','Latte','Cappuccino' : ").lower()
        drink = a_menu.find_drink(choice)
        if drink is not None:
            if a_coffeemaker.is_resource_sufficient(drink):
                if a_moneymachine.make_payment(drink.cost):
                    a_coffeemaker.make_coffee(drink)
        elif choice == "report":
            os.system("cls" if os.name == "nt" else "clear")
            a_coffeemaker.report()
        elif choice == "profit":
            os.system("cls" if os.name == "nt" else "clear")
            a_moneymachine.report()


if __name__ == "__main__":
    main()
