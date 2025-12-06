#!/usr/bin/python3
"""
This module provides a function for adding two numbers.

It ensures that both inputs are integers or floats, converting floats
to integers before performing the addition. Non-finite values such as
NaN or infinity are rejected with a TypeError.
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    The function accepts integers and floats only, and converts
    floats to integers before performing the addition.
    """

    # Reject NaN
    if isinstance(a, float) and a != a:
        raise TypeError("a must be an integer")
    if isinstance(b, float) and b != b:
        raise TypeError("b must be an integer")

    # Reject infinity (float('inf'), float('-inf'))
    if isinstance(a, float) and (a == float('inf') or a == float('-inf')):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b == float('inf') or b == float('-inf')):
        raise TypeError("b must be an integer")

    # Validate types
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
