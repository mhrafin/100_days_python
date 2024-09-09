import os

import question_model
from quiz_brain import QuizBrain

os.system("cls" if os.name == "nt" else "clear")

question_bank = question_model.create_questions()
quizzer = QuizBrain(question_bank)

for q in question_bank:
    result = quizzer.next_question()

print(f"Your Score: {quizzer.score}/{quizzer.question_no}")
