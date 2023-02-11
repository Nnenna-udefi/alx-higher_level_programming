#!/usr/bin/python3
"""Defines a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square that inherits from the rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the Square

        Args:
            size(int): size of the square
            x (int): x cordinates of the square
            y (int): y cordinates if the square
            id (int): identity of the new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets/sets the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
        
    def __str__(self):
        """Update the class Rectangle by overriding the __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute

        *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]

        for key, value in kwargs.items():
            setattr(self, key, value)
