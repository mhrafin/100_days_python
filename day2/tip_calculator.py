print("Welcome to Tip Calculator!")
bill = float(input("How much is the bill? \n"))
tip = float(input("How much tip would you like to give? \n"))
people = int(input("How many people to split the bill? \n"))

total = (bill+tip/100*bill)/people

print(f"Each person should pay {round(total,2)}")