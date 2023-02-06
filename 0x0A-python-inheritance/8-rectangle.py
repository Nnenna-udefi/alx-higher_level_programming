#!/usr/bin/python3
"""Defines a Rectangle that inherits from Base Geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a Rectanlge inherited from base geometry"""

    def __init__(self, width, height):
        """Intialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle, private
                and positive integer validated by integer_validator
            height (int): The height of the new Rectangle, porivate
                and positive integer
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
