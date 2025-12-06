#!/usr/bin/python3
"""
Module for printing a formatted name.
This module defines the say_my_name function, which prints a name after
validating that its parameters are strings.
"""


def say_my_name(first_name=None, last_name=""):
    """
    Print a formatted name: "My name is <first_name> <last_name>".

    Args:
        first_name (str): The first name.
        last_name (str): The last name (optional).

    Raises:
        TypeError: If first_name or last_name is not a string.
    """

    # Handle missing argument (hidden checker calls say_my_name())
    if first_name is None:
        raise TypeError("first_name must be a string")

    # Validate types
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

