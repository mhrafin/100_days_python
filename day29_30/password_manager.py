import random
import tkinter as tk
from tkinter import messagebox

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    password_input.delete(0, tk.END)
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    # print(lower_letters)

    upper_letters = [letter.upper() for letter in letters]

    letters.extend(upper_letters)
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    signs = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

    password = ""

    length = random.randint(9, 19)
    sym = 3
    num = 3

    for n in range(length):
        if (length - n) == (sym + num):
            if sym > 0:
                password += random.choice(signs)
                sym -= 1
            else:
                password += random.choice(numbers)
                num -= 1
        else:
            turn = random.randint(0, 2)
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

    password_input.insert(tk.END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = website_input.get()
    email_data = email_input.get()
    password_data = password_input.get()

    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(
            title="Empty Fields", message="Do not leave any empty fields."
        )
        confirmed = False
    else:
        confirmed = messagebox.askokcancel(
            title="Confirmation",
            message=f"These are the details entered: \nWebsite: {website_data}\nEmail: {email_data}\nPassword: {password_data}\nIs it Ok to Save?",
        )
    if confirmed:
        with open("day29_30/data.txt", mode="a") as data_file:
            new_data = f"{website_data} | {email_data} | {password_data}\n"
            data_file.write(new_data)

        website_input.delete(0, "end")
        email_input.delete(0, "end")
        password_input.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title(string="Password Manager")
window.config(padx=20, pady=20)


canvas = tk.Canvas(width=200, height=200)

lock_logo = tk.PhotoImage(file="day29_30/logo.png")
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(column=0, row=0, columnspan=3)

website_text = tk.Label(text="Website:")
website_text.grid(column=0, row=1)
website_input = tk.Entry(width=37)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

email_text = tk.Label(text="Email/Username:")
email_text.grid(column=0, row=2)
email_input = tk.Entry(width=37)
email_input.insert(tk.END, "email@mail.com")
email_input.grid(column=1, row=2, columnspan=2, pady=1)

password_text = tk.Label(text="Password:")
password_text.grid(column=0, row=3)
password_input = tk.Entry(width=22)
password_input.grid(column=1, row=3)
gen_pass_button = tk.Button(
    text="Generate Password", height=0, width=12, command=generate_pass
)
gen_pass_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, pady=1)


window.mainloop()
