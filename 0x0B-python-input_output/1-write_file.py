#!/usr/bin/python3
"""Defines a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """The file is utf8 encoded and returns the number of characters written
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
