#!/usr/bin/python3
"""Defines a function thay prints"""


def say_my_name(first_name, last_name=""):
    """Prints the first and last name.

    Raise:
    TyoeError if first and last name is not a string"""

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
