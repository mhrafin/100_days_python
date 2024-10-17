from tkinter import *
from tkinter import ttk

VALUES = ["Mile", "Kilometer"]


def calculate():
    from_ = combo1.get()
    from_int = float(input.get())

    to = combo2.get()   
    output = 0

    if from_ == to:
        output = from_int
        result.config(text=output)
    elif to == "Kilometer":
        output = round((from_int / 0.62), 2)
    elif to == "Mile":
        output = round((from_int * 0.62), 2)

    result.config(text=output)


window = Tk()
window.title("Mile and Kilometer Converter")
window.minsize(width=400, height=300)
window.config(padx=50, pady=50)

title = Label(text="Converter", font=("Arial", 16, "bold"))
title.grid(column=0, row=0, columnspan=3)
title.config( pady=20)

input = Entry(width=5)
input.grid(column=1, row=1)
input.config()

combo1 = ttk.Combobox(state="readonly", width=7, values=VALUES)
combo1.grid(column=2, row=1, padx=10, pady=10)

combo2 = ttk.Combobox(state="readonly", width=7, values=VALUES)
combo2.grid(column=2, row=2, padx=10, pady=10)

text = Label(text="is equal to", font=("Arial", 11))
text.grid(column=0, row=2)

result = Label(text="0", font=("Arial", 11))
result.grid(column=1, row=2)
result.config(padx=40)

button = Button(text="Calculate", command=calculate)
button.grid(column=0, row=3, columnspan=3)


window.mainloop()
