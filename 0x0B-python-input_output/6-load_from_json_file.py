#!/usr/bin/python3
"""Defines a json-object function"""
import json


def load_from_json_file(filename):
    """The function creates an Object from a JSON file"""
    with open(filename) as f:
        json.load(f)
