import data


class Question:
    def __init__(self, text, answer) -> None:
        self.text = text
        self.answer = answer


def create_questions():
    """Takes data (List of dictionaries with key 'text' and 'answer') from data.py and returns a list filled with Question objects."""
    question_bank = []
    for i in data.question_data:
        question_bank.append(Question(i["question"], i["correct_answer"]))
    return question_bank
