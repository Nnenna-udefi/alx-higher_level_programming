#!/usr/bin/python3
"""Defines a pascal triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the
    Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        angle = triangle[-1]
        tmp = [1]
        for i in range(len(angle) - 1):
            tmp.append(angle[i] + angle[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
