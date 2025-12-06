#!/usr/bin/python3
"""
Module that defines a safe integer addition function.
It validates types, rejects NaN and infinite floats,
and cleanly handles overflow during integer conversion.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats after validating and safely converting them.

    Floats are accepted only if they represent finite numeric values.
    NaN and infinite values are rejected because they cannot be reliably
    converted to integers. Unsupported types raise a TypeError.

    Args:
        a (int or float): First operand.
        b (int or float): Second operand, default is 98.

    Returns:
        int: The sum of the integer-converted operands.

    Raises:
        TypeError: If a or b is not a valid integer or float.
    """
    # 1. Validate types
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # 2. Reject NaN explicitly
    # NaN != NaN is the only true test for NaN in Python
    if isinstance(a, float) and (a != a):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b != b):
        raise TypeError("b must be an integer")

    # 3. Reject infinite floats BEFORE casting to int
    if isinstance(a, float) and (a == float('inf') or a == float('-inf')):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b == float('inf') or b == float('-inf')):
        raise TypeError("b must be an integer")

    # 4. Try converting safely (catch overflow or invalid float states)
    try:
        a = int(a)
    except Exception:
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except Exception:
        raise TypeError("b must be an integer")

    return a + b
