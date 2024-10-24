import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quiz Time!")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score = tk.Label(
            text=f"Score: {self.quiz.score}/{self.quiz.question_number}",
            justify="center",
            foreground="white",
            background=THEME_COLOR,
        )
        self.score.grid(column=1, row=0)

        self.canvas = tk.Canvas(width=300, height=250, background="white")
        self.quiz_q = self.canvas.create_text(
            150, 125, text="Question", font=("Arial", 12, "italic"), width=280
        )
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=50)

        self.true_button_png = tk.PhotoImage(file="day34/images/true.png")
        self.true_button = tk.Button(
            width=100,
            height=97,
            image=self.true_button_png,
            highlightthickness=0,
            bd=0,
            background=THEME_COLOR,
            command=self.true_pressed
        )
        self.true_button.grid(column=0, row=2)

        self.false_button_png = tk.PhotoImage(file="day34/images/false.png")
        self.false_button = tk.Button(
            width=100,
            height=97,
            image=self.false_button_png,
            highlightthickness=0,
            bd=0,
            background=THEME_COLOR,
            command=self.false_pressed
        )
        self.false_button.grid(column=1, row=2)

        self.get_next_q()

        self.window.mainloop()

    def get_next_q(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_q, text=question)
        else:
            self.canvas.itemconfig(self.quiz_q, text="Quiz is Over!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        

    def true_pressed(self):
        #self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        #self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.window.after(1000, func=self.get_next_q)

    def canvas_green(self):
        self.canvas.config(background="green")













