#!/usr/bin/python3
"""Defines an integer addition function.
    The function adds two integers
    a and b
    and returns the addition of a and b
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.
    Args: a, b.
    Raises: TypeError: If either of a or b is a non-integer and non-float."""

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
