#!/usr/bin/python3
"""Defines a student class"""


class Student:
    """
    Represent a student
    Args:
        first_name(str): The first name of the student.
        last_name(str): The last name of the student.
        age(int): The age of the student.
    """
    def __init__(self, first_name, last_name, age):
        """Initializes the public attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student"""
        return self.__dict__
