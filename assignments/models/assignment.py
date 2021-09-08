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
        self.tasks = [Task(int(k), v['answer'], v['variable'], v['description']) for k, v in self.assignment.get('tasks').items()]
        self.questions = self.assignment.get('questions')

    def get_task(self, nr) -> Task:
        """Gets appropriate task for given task nr"""

        return self.tasks[[t.nr for t in self.tasks].index(nr)]

    def assert_tasks(self, func_dict: dict) -> None:
        """Asserts functions with given task nr"""

        for nr, func in func_dict.items():
            task = self.get_task(nr)

            print(f' Task nr {task.nr} '.center(30, '='))
            print(f'{task.description}\nVariables: {task.variables}\nAnswer: {task.answer}')

            assert func(**task.variables) == task.answer

            print('Pass!')

    def show_questions(self) -> None:
        print('\n\n'.join(f'{k}: {v["question"]}\n {v["answer"]}' for k, v in self.questions.items()))

    def __repr__(self) -> str:
        return '\n'.join(f'{k}: {v}' for k, v in self.__dict__.items())

