#!/usr/bin/python3
"""Defines a function that reads a text file"""


def read_file(filename=""):
    """file is utf8 encoded and prints to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
