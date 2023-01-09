#!/usr/bin/python3

"""11-student
Contains class Student
"""


class Student:
    """Based on module 10-student, adds method reload_from_json"""

    def __init__(self, first_name, last_name, age):
        """Initializes the attributes of this class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves the dictionary representation of Student,
        by selecting the attributes passed in @attrs"""

        if type(attrs) is not list:
            return self.__dict__

        attributes = {}
        for i in attrs:
            if i in self.__dict__.keys():
                attributes[i] = getattr(self, i)

        return attributes

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        Args:
            json (dict): JSON dict to get attributes and their values from
        """
        for i, j in zip(json.keys(), json.values()):
            setattr(self, i, j)
