"""
Custom exception class
"""


class WrongAnswer(Exception):
    def __init__(self, answer: int, correct_answer: int, message: str = 'Wrong answer'):
        self.message = message
        self.answer = answer
        self.correct_answer = correct_answer

    def __str__(self):
        return f'{self.message}:\nComputed result = {self.answer}\nCorrect result = {self.correct_answer}'
