#!/usr/bin/python3

"""9-student
Contains class Student
"""


class Student:
    """Base class for subsequent tasks"""

    def __init__(self, first_name, last_name, age):
        """Initializes the attributes of this class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves the dictionary representation of Student"""
        return self.__dict__
