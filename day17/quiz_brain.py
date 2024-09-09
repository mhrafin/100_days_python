from question_model import Question


class QuizBrain:
    def __init__(self, question_list: list) -> None:
        self.question_no = 0
        self.list_of_Question_objects = question_list
        self.score = 0

    def next_question(self):
        """Asks the current question. Records the user answer from input and checks the answer."""
        current_question: Question = self.list_of_Question_objects[self.question_no]

        self.question_no += 1

        user_answer = input(
            f"Q.{self.question_no}. {current_question.text} (TRUE/FALSE) "
        ).lower()
        # print(f"True answer: {current_question.answer.lower()} || Your answer: {user_answer}")

        self.check_answer(user_answer, current_question)

    def check_answer(self, user_answer, current_question: Question):
        """Checks the answer. Takes in user's answer as str and current question as Question object."""
        if user_answer == current_question.answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")

        print(f"The answer was {current_question.answer}")
        print("\n")

        # print(user_answer == current_question.answer.lower())
        # return user_answer == current_question.answer.lower()
