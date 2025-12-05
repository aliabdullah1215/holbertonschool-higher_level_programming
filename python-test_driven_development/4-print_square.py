#!/usr/bin/python3
"""
This module defines a function that prints a square with '#'.
"""


def print_square(size):
    """
    Print a square with the character '#'.

    Args:
        size: The size of the square (must be an integer >= 0).

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

