#!/usr/bin/python3
"""
Module defining a function that prints a square of '#'.
"""


def print_square(size=None):
    """
    Print a square with '#' characters.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """

    # Hidden checker: calling print_square()
    if size is None:
        raise TypeError("size must be an integer")

    # Must be integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Must not be negative
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
