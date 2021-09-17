from functools import lru_cache

"""
Functions for running the assignments
"""


def sum_list(numbers: list) -> int:
    """Sums a list of ints with pythons built in sum() function"""

    return sum(numbers)


def convert_int(n: int) -> str:
    """Converts an int to a string"""

    return str(n)


def recursive_sum(item: list) -> int:
    """Calculates the sum of a nested list with recursion"""

    return item if isinstance(item, int) else sum_list([recursive_sum(i) for i in item])


@lru_cache
def fibonacci(n: int) -> int:
    """
    Calculate the nth number of the fibonacci sequence using recursion.
    We could memoize this ourselves but I prefer to use lru_cache to keep the function clean.
    """

    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


def sum_integer(number: int) -> int:
    """Calculates the sum of integers in a number e.g 123 -> 6"""

    return sum_list([int(i) for i in convert_int(number)])


def gcd(a: int, b: int) -> int:
    """
    Calculated the GCD recursively according to the Euclidean algorithm gcd(a,b) = gcd(b, r).
    Where r is the remainder of a divided by b.
    """

    return a if not b else gcd(b, a % b)
