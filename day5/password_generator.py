import random

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#print(lower_letters)

upper_letters = []
for letter in letters:
    upper_letters.append(letter.upper())

#print(upper_letters)
letters.extend(upper_letters)
numbers = ['1','2','3','4','5','6','7','8','9','0']
signs = ["!","@","#","$","%","^","&","*","(",")"]

password = ""

print("Welcome to password generator!")
length = int(input("How many letters would you like in your password?\n"))
sym = int(input("How many symbols would you like?\n"))
num = int(input("How many numbers would you like?\n"))

for each in range(length):
    if (length-each) == (sym+num):
        if sym > 0:
            password += random.choice(signs)
            sym -= 1
        else:
            password += random.choice(numbers)
            num -= 1
    else:
        turn = random.randint(0,2)
        if turn == 0:
            password += random.choice(letters)
            continue
        
        if turn == 1 and sym > 0:
            password += random.choice(signs)
            sym -= 1
            continue
        elif turn == 2 and num > 0:
            password += random.choice(numbers)
            num -= 1
            continue
        else:
            password += random.choice(letters)
            continue

print(f"Here is your password: {password}")
    