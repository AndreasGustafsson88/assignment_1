"""
Main class for tasks
"""


class Task:

    def __init__(self, nr: int, answer: str, variable, description: str):
        self.nr = nr
        self.answer = answer
        self.variables = variable
        self.description = description

    def __repr__(self):
        return '\n'.join(f'{k}: {v}' for k, v in self.__dict__.items())
