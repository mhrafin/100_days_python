import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier New"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 1
marks = ""
timer = None
timer_started = False


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global rep
    rep = 1

    global marks
    marks = ""
    check_marks.config(text=marks)

    start_btn.config(state="active")
    reset_btn.config(state="disabled")

    window.after_cancel(timer)

    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global rep
    global marks

    start_btn.config(state="disabled")
    reset_btn.config(state="active")

    work_min_s = WORK_MIN * 60
    short_break_min_s = SHORT_BREAK_MIN * 60
    long_break_min_s = LONG_BREAK_MIN * 60

    if rep in [1, 3, 5, 7]:
        title.config(text="Work", fg=RED)
        check_marks.config(text=marks)
        rep += 1

        count_down(work_min_s)
    elif rep in [8]:
        title.config(text="Break", fg=GREEN)
        marks += "✓"
        check_marks.config(text=marks)
        rep = 1
        marks = ""
        count_down(long_break_min_s)

    elif rep in [2, 4, 6]:
        title.config(text="Break", fg=PINK)
        marks += "✓"
        check_marks.config(text=marks)
        rep += 1
        count_down(short_break_min_s)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(second):
    global timer
    current_min = second // 60
    current_sec = second % 60
    if current_sec in range(0, 10):
        current_sec = "0" + str(current_sec)

    canvas.itemconfig(timer_text, text=f"{current_min}:{current_sec}")
    if second > 0:
        timer = window.after(1000, count_down, second - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoros")
window.config(padx=100, pady=50, background=YELLOW)


# Canvas
canvas = tk.Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)

tomato_img = tk.PhotoImage(file="day28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(
    100,
    130,
    text="00:00",
    fill="white",
    font=(
        FONT_NAME,
        35,
        "bold",
    ),
)

canvas.grid(column=1, row=1)


# Title
title = tk.Label(
    text="Timer", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 50)
)
title.grid(column=1, row=0)

# Start Button
start_btn = tk.Button(
    text="Start", background="white", command=start_timer, highlightthickness=0
)
start_btn.grid(column=0, row=2)

# Reset Button
reset_btn = tk.Button(
    text="Reset",
    background="white",
    command=reset_timer,
    highlightthickness=0,
    state="disabled",
)
reset_btn.grid(column=2, row=2)

# Check mark
check_marks = tk.Label(
    text="", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 26)
)
check_marks.grid(column=1, row=3)

window.mainloop()
