import datetime
import json
from assignments.models.task import Task

"""
Main class for assignments
"""


class Assignment:
    def __init__(self, number: int, date: str):
        self.number = number
        self.deadline = datetime.datetime.strptime(date, '%d-%m-%Y')
        self.assignment = json.load(open(f'assignments/data/assignment_{self.number}.json'))
        self.tasks = [Task(int(k), **v) for k, v in self.assignment.get('tasks').items()]
        self.questions = self.assignment.get('questions')

    def assert_tasks(self) -> None:
        """Loops through all tasks in the assignment and calls evaluate"""

        [task.evaluate() for task in self.tasks]

    def show_questions(self) -> None:
        print('\n\n'.join(f'{k}: {v["question"]}\n {v["answer"]}' for k, v in self.questions.items()))

    def __repr__(self) -> str:
        return '\n'.join(f'{k}: {v}' for k, v in self.__dict__.items())

