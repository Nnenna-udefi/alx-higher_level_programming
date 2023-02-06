#!/usr/bin/python3
"""Defines a rebel class"""


class MyInt(int):
    """MyInt class inherits from int
    MyInt has == and != operators inverted
    """

    def __eq__(self, value):
        """Override == operator with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
