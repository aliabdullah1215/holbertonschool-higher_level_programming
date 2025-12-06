#!/usr/bin/python3
"""
Module for safely adding two numbers.
Rejects NaN, infinite floats, and overflow values.
"""


def valid_number(n, var_name):
    """
    Validate that n is an integer or a finite float.

    Args:
        n: value to validate
        var_name: string for the error message ("a" or "b")

    Raises:
        TypeError: If n is not a valid integer/float
    """

    # Check type
    if not isinstance(n, (int, float)):
        raise TypeError(f"{var_name} must be an integer")

    # NaN check (only NaN satisfies n != n)
    if isinstance(n, float) and n != n:
        raise TypeError(f"{var_name} must be an integer")

    # Infinity / overflow detection
    # (x + 1 == x) is only true for +inf or -inf
    if isinstance(n, float) and (n + 1 == n):
        raise TypeError(f"{var_name} must be an integer")

    return int(n)


def add_integer(a, b=98):
    """
    Add two integers or floats safely and return their integer sum.

    Args:
        a (int or float): first number
        b (int or float): second number (default = 98)

    Returns:
        int: integer sum of a and b

    Raises:
        TypeError: If a or b is not a valid finite number
    """

    a = valid_number(a, "a")
    b = valid_number(b, "b")

    return a + b
