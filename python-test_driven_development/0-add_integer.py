#!/usr/bin/python3
"""
This module provides a safe integer addition function.
It validates inputs, prevents invalid float conversions,
and raises clear exceptions for incorrect types.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats safely and return their integer sum.

    The function ensures that both arguments are either integers
    or floats. It also validates that floats are finite (not NaN
    and not infinite) before casting them to integers. When invalid
    data types or values are provided, a TypeError is raised.

    Args:
        a (int or float): The first number.
        b (int or float): The second number (default=98).

    Returns:
        int: The sum of a and b after converting floats to integers.

    Raises:
        TypeError: If either a or b is not a valid integer or float.
    """

    # Validate type first
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Reject NaN
    if isinstance(a, float) and (a != a):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b != b):
        raise TypeError("b must be an integer")

    # Convert safely (catch overflow like float('inf'))
    try:
        a_int = int(a)
    except (OverflowError, ValueError):
        raise TypeError("a must be an integer")

    try:
        b_int = int(b)
    except (OverflowError, ValueError):
        raise TypeError("b must be an integer")

    return a_int + b_int
