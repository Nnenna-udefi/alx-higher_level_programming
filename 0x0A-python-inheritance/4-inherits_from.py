#!/usr/bin/python3
"""Defines a sub class function"""


def inherits_from(obj, a_class):
    """Return True if the object is an instance of a class that inherited
        directly or indirectly from the specified class.
        Otherwise: returns False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
