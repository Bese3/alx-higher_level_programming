#!/usr/bin/python3

"""7-base_geometry
Contains class BaseGeometry
"""


class BaseGeometry:
    """
    Empty class with just one method
    """
    def area(self):
        """
        Function is not implemented yet, so it raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value=None):
        """
        Raises appropriate exceptions with messages. Doesn't do anything
        in particular
        """
        try:
            if type(value) != int:
                raise TypeError(name + " must be an integer")
            if value <= 0:
                raise ValueError(name + " must be greater than 0")
        except NameError:
            raise TypeError(name + " must be an integer")
