#!/usr/bin/python3
"""Defines a class Square inherited from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits properties from Rectangle

    Args: size (private and positive integer)
    """
    def __init__(self, size):
        """Initialize size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
