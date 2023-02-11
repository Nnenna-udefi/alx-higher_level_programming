#!/usr/bin/python3
"""Defines a class Base."""


class Base:
    """Represent a base of all the classes in this project

    Private Class Attribute:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0
    def __init__(self, id=None):
        """Initializes the base
        Args:
            id(int) - identity of the base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
