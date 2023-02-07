#!/usr/bin/python3
"""Defines a function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """It inserts a line of text to a file, after each line
    containing a specific string
    Args:
        filename(str): name of the file
        search-strings: specific string to search for in the file
        new_string (str): The string to insert
    """
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
