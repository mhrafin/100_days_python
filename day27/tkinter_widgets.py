from tkinter import (
    Button,
    Checkbutton,
    Entry,
    IntVar,
    Label,
    Listbox,
    Radiobutton,
    Scale,
    Spinbox,
    Text,
    Tk,
)

window = Tk()
window.title(string="Widgets Demo")
window.minsize(width=400, height=800)


# Label
label = Label(text="This is new text", font=("Arial", 12, "bold"))
label.pack()


# Button
def button_clicked():
    print("Button Clicked!")


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry. Basically works like an input
entry = Entry(width=30)
entry.insert(0, string="Some text to begin with")
print(entry.get())
entry.pack()

# Text
text_box = Text(height=5, width=30)
text_box.focus()
text_box.insert(index="end", chars="Example of a multi-line text.")
print(text_box.get("1.0", "end"))
text_box.pack()


# Spinbox
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=2, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbox
def checkbutton_used():
    print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(
    text="Is on?", variable=checked_state, command=checkbutton_used
)
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(
    text="Option 1", value=1, variable=radio_state, command=radio_used
)
radiobutton2 = Radiobutton(
    text="Option 2", value=2, variable=radio_state, command=radio_used
)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["apple", "banana", "orange", "pear"]

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
