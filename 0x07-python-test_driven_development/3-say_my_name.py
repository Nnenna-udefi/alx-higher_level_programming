#!/usr/bin/python3
"""Defines a function thay prints"""


def say_my_name(first_name, last_name=""):
    """Prints the first and last name.

    Raise:
    TypeError if first and last name is not a string"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
