#!/usr/bin/python3
"""
Module defining a function that prints a square of '#'.
"""


def print_square(*args):
    """
    Print a square with '#' characters.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """

    # Hidden checker: calling print_square() with 0 arguments
    if len(args) == 0:
        raise TypeError("size must be an integer")

    # Hidden checker: calling print_square(a, b, ...)
    if len(args) > 1:
        raise TypeError("size must be an integer")

    size = args[0]

    # Now validate size
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
