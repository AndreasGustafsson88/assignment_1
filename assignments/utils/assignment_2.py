import time
from functools import reduce
from typing import Iterator

"""
Functions needed for running assignment 2
"""


# ---- NOT PART OF ASSIGNMENT! -----
def run_10_time(func):
    """Only for task evaluation, creates and runs iterator 10 times"""
    gen = func()

    return lambda: [next(gen) for _ in range(10)]


def timer(nr_lapses: int):
    """runs function n nr of times and times each iteration, returns average time for each iteration"""

    def timer_decorator(func):
        def wrapper(*args, **kwargs):
            total_time = 0
            for _ in range(nr_lapses):
                start = time.time_ns()
                func(*args, **kwargs)
                stop = time.time_ns()
                total_time += stop - start
            print(f'Average time for {nr_lapses} runs: {total_time / nr_lapses}')

        return wrapper

    return timer_decorator


# --------------------------------


@run_10_time
def fibonacci_generator() -> Iterator[int]:  # === 1 ===
    """
    Fibonacci generator
    ...

    Will yield next nr in sequence each time it's called
    Initiates with start values: 0, 1. For each iteration adds values E.g a = 1 & b = 1 + 0
    """

    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# @timer(10)
def return_str(values: list[str]) -> list[list[str]]:  # === 2 ===
    """
    Returns each word as a list instead of a str

    Comparing with lambda solution (Not part of assignment).
    """

    # return list(map(lambda val: [l for l in val], values))  # ns: 4100270.0
    return [[letter for letter in word] for word in values]  # ns: 2999210.0


def repack_dict(values: dict) -> list[dict]:  # === 3 ===
    """
    Changes dict structure. Starts with unpacking previous or empty list for first iteration (*a).
    Uses new python union operator | to join two dicts. Dict from values[key] and newly created name: key
    """

    return reduce(lambda a, key: [*a, values[key] | {'name': key}], values, [])


def lowercase(func):  # === 4 ===
    """Decorator function to convert result given func to lowercase"""

    return lambda *args, **kwargs: func(*args, **kwargs).lower()


def tired(_func=None, seconds: int = 5):  # === 5 ===
    """
    Decorator to make system sleep for n number of seconds.

    This solution needs the arg to be given with kw. E.g seconds=2.
    But also leaves the option to leave decorator blank and defaults to chosen default value.
    """

    def tired_decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)

        return wrapper

    return tired_decorator if not _func else tired_decorator(_func)


@tired(seconds=2)
@lowercase
def get_name():
    return 'John Doe'


def filter_out(values: list[int]) -> list[int]:  # === 6 ===
    """Uses built in filter to return a list with numbers lower than 42"""

    return list(filter(lambda n: n < 42, values))
