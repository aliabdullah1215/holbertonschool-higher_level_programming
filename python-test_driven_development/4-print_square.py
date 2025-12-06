#!/usr/bin/python3
"""
Module defining a function that prints a square with '#'.
"""


def print_square(size):
    """
    Print a square with '#' characters.

    Args:
        size (int): The size of the square (number of rows and columns).

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

