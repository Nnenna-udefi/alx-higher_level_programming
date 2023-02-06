#!/usr/bin/python3
"""DEfines a class that inherits from another"""


class MyList(list):
    """MyList class inherits from the list class"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
