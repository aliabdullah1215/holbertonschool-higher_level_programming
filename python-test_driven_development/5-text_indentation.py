#!/usr/bin/python3
"""
This module defines a function that prints indented text.
"""


def text_indentation(text):
    """
    Print text with 2 new lines after each '.', '?' or ':'.

    Args:
        text: The input string.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Temporary buffer to accumulate characters
    buffer = ""

    for char in text:
        buffer += char
        if char in ".?:":
            print(buffer.strip())
            print()
            buffer = ""

    # Print any remaining text (if no punctuation at end)
    if buffer.strip():
        print(buffer.strip(), end="")
