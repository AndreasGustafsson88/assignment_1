from assignments.models.assignment import Assignment
from assignments.utils.functions import *

"""
Course: Effective Python - Assignment 1
Student: Andreas Gustafsson
"""


def run_assignment(assignment: Assignment) -> None:
    """Main function for evaluating assignments"""

    assignment.assert_tasks(
        {
            1: sum_list,
            2: convert_int,
            3: recursive_sum,
            5: fibonacci,
            6: sum_integer,
            11: gcd
        }
    )

    assignment.show_questions()

    """
    Om du vill köra koden eller läsa svar på frågorna i json så klistrar jag in resultatet av show_questions():
    
    1: Explain what a variable is
     A variable is a name that refers to a value. The variable type is whatever its value is.
    
    2: Explain what a function is
     A named set of code statements that performs a task.
    
    3: Explain what a program is
     A Program is a set of instructions of how to perform a task.
    
    4: Explain what makes a program effective
     The program performs the computation it is meant to do in an clear and efficient manner.
    
    5: Explain what effective programming is
     Effective programming is: 
    -	Good understanding and use of algorithms, code reuse
    -	Clear intentions and unambiguous code
    -	Proper documentation
    """

if __name__ == "__main__":
    assignment_1 = Assignment(1, '13-09-2021')
    run_assignment(assignment_1)
