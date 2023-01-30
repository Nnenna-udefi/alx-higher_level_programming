#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Represent a rectangle
    Instance Attribute:
        Width: Raise TypeError if width is not an integer
            ValueError if width is less than 0
        Height: Raise Type Error if Height is not an integer
            ValueError if height is less than 0
    Return height and width
    """
    def __init__(self, width=0, height=0):
        """Initializes a new Class Rectangle instance."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
