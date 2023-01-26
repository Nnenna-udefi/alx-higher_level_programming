#!/usr/bin/python3
""" defines a function that devides all the elements of a matrix"""


def matrix_divided(matrix, div):
    """Divide all the elements in a matrix.

    matrix must be a list of lists of integers or floats
    raise:
    TypeError if matrix is not a list of integers or floats
    
    Each row must be of equal size
    Raise:
    TypeError if not

    div must be of int or float tyoe
    Raise:
    TypeError if not

    div can't be equal to O
    Raise:
    ZeroDivisionError if div is equal to 0

    All elements of the matrix should be divided by div, rounded to 2 decimal places

    Function should return a new matrix."""

    if type(div) is not (int, float):
        raise TypeError(div must be a number)
    if div == 0:
        raise ZeroDivisionError(division by Zero)
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats.")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of \
                        integers/floats.")
    return [[round(i / div, 2) for i in row] for row in matrix]
