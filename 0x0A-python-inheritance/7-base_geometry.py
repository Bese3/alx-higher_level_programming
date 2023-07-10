#!/usr/bin/python3
"""
a class to build upon next project
"""


class BaseGeometry():
    """
    class with method appended
    """
    def area(self):
        """
        The function area() raises an exception indicating
        that it is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        The function `integer_validator` checks
        if a given value is an integer and greater than 0,
        and raises appropriate errors if not.
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
