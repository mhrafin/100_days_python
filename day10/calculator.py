from calculator_ascii import *
import sys

print(calc_logo)
print(calc_ascii+ "\n")

# Takes two numbers and operator, returns the result.
def calculator(first, operator, second):
    if chr(operator) == "+":
        return first + second
    elif chr(operator) == "-":
        return first - second
    elif chr(operator) == "*":
        return first * second
    elif chr(operator) == "/":
        return first / second

def main_calc():
    first_key = float(input("First number: "))
    print("+\n-\n*\n/")
    while True:    
        operator = ord(input("Operator: "))
        second_key = float(input("Second number: "))
        
        result = calculator(first_key,operator,second_key)    
        print(f"{first_key} {chr(operator)} {second_key} = {result}")

        # Loops with the result as the first number or resets or exits.
        proceed = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation.\nType 'exit' to exit the calculator.\n").lower()
        if proceed == "y":
            first_key = result
        elif proceed == "n":
            main_calc()
        else:
            print("Exiting the Calculator.")
            sys.exit()

main_calc()