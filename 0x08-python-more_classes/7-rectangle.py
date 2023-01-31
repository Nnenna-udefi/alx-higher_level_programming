#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Represent a rectangle
    Class Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
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
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        peri = self.__width + self.__height
        return 2 * peri

    def __str__(self):
        """Return the printable representation of the Rectangle
        and prints the character # to represent the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rec = []
        for x in range(self.__height):
            [rec.append(str(self.print_symbol)) for i in range(self.__width)]
            if x != self.__height - 1:
                rec.append("\n")
        return("".join(rec))

    def __repr__(self):
        """reyurn the string representation of.the rectangle"""
        rec = "Rectangle(" + str(self.__width)
        rec = ", " + str(self.__height) + ")"
        return rec

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
