from dataclasses import dataclass
from assignments.models.error import WrongAnswer
from assignments.utils import functions

"""
Main class for tasks
"""


@dataclass
class Task:
    nr: int
    answer: int
    _function: str
    variables: dict
    description: str

    @property
    def function(self):
        """Fetches corresponding function based on function name from function module"""

        return getattr(functions, self._function)

    def evaluate(self) -> None:
        """Evaluates answer given by function and correct answer for the task"""

        print(f' Task nr {self.nr} '.center(30, '='))
        print(f'{self.description}\nVariables: {self.variables}\nAnswer: {self.answer}')

        if not self.function(**self.variables) == self.answer:
            raise WrongAnswer(self.function(**self.variables), self.answer)

        print('Pass!')
