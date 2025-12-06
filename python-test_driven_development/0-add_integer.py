#!/usr/bin/python3
"""
This module provides a function for adding two numbers.
The function ensures that the inputs are integers or floats
and raises appropriate errors when invalid types are provided.
It is part of the Python Test-Driven Development project.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats and return the result as an integer.

    The function accepts two arguments, casts floats to integers,
    and ensures both values are numeric. If non-numeric values are
    passed, a TypeError is raised with a clear error message.

    Args:
        a (int or float): The first number.
        b (int or float): The second number, default is 98.

    Returns:
        int: The integer result of adding a and b.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
