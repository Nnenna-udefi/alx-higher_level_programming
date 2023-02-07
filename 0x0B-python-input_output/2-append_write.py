#!/usr/bin/python3
"""Defines a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """file that is utf 8 encoded and returns the number of characters added
    Args:
       filename(str): file to append
       text(str): the text to append to the file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
