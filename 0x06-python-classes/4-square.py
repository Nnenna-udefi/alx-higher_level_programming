#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        """Initialize a new square."""

    @property
    def size(self):
        """to retrieve the attribute size"""
        return (self.__size)
    @size.setter
    def size(self, value):
        """sets the value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
