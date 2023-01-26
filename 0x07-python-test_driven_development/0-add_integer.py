#!/usr/bin/python3
"""addition of two integers"""

def add_integer(a, b=98):
    """Returns an integer: the addition of a and b
    a and b must be integers or floats

    Raises:
    TyoeError, if a and be is not an integer or float."""

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
