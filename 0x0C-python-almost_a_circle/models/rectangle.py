#!/usr/bin/python3
"""Defines a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle that inherits the project's base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle

        Args:
            width(int): width of the rectangle
            height(int): height of he rectangle
            x (int): x cordinates of the rectangle
            y (int): y cordinates if the rectangle
            id (int): identity of the new rectangle
            id is called with a super class with use the logic of the __init_
            of the Base class.

        Raise:
            TypeError: If either of width or height is not an int.
            TypeError: If either of x or y is not an int.
            ValueError: If either of width or height <= 0.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets/sets the width of the rectangle"""
        return self.__width = value

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets/sets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """sets/gets the x coordinates of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """sets/gets the y coordinates of the rectanlge"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        for i in range(self.y):
            print("")
        for j in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Update the class Rectangle by overriding the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute

        *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

        for key, value in kwargs.items():
            setattr(self, key, value)
