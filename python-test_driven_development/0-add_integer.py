#!/usr/bin/python3
"""
This module provides a function for adding two numbers.

It ensures that both inputs are integers or floats, converting floats
to integers before performing the addition. If the inputs are not valid
numeric types, the function raises a TypeError with a clear message.
This module is part of the test-driven development tasks.
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    The function accepts integers and floats only, and converts
    floats to integers before performing the addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
