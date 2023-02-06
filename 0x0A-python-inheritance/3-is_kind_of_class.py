#!/usr/bin/python3
"""Defines a function that is an instance of an object if it is inherited
    from a specifieed class.
"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of
        or if the object is an instance of a class the inherited from
        the specified class
        Otherwise: Return False
    """
    if isinstance(obj, a_class):
        return True
    return False
