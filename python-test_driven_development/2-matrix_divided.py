#!/usr/bin/python3
"""
This module defines a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number and return a new matrix.

    Args:
        matrix: A list of lists containing integers or floats.
        div: The number to divide all elements of the matrix by.

    Returns:
        A new matrix with all values divided by div and rounded to 2 decimals.

    Raises:
        TypeError: If matrix is not a list of lists of numbers.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    # Validate matrix structure
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate rows and elements
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # New matrix
    return [[round(item / div, 2) for item in row] for row in matrix]
