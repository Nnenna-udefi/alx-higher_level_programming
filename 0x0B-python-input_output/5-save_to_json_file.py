#!/usr/bin/python3
"""function that writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ARGS:
            my_obj(str): object to be written to the textfile
            filename: text file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
