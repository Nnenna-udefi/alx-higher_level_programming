#!/usr/bin/python3
"""Defines a function that checks the object instace of a class"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the
        specified class
        Otherwise: returns False.
    """
    if type(obj) == a_class:
        return True
    return False
