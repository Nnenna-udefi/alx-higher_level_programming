#!/usr/bin/python3
"""Defines a base Geometry function"""


class BaseGeometry:
    """Represents a base geometry"""

    def area(self):
        """Raises an exception since area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as an integer

        ARGs:
            value (type int)
            name (type str)
        Raise:
            TypeEror if value is not an integer
            ValueError if value is less or equal to 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
