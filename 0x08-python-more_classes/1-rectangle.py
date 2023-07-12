#!/usr/bin/python3


"""
Module containing class Rectangle
"""


class Rectangle:
    """
    A rectangle that has a width and height. Both are 0 by default.
    """
    def __init__(self, width=0, height=0):
        """
        width and height are initialized here. Appropriate error is printed if
        passed vars are incorrect

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        Attributes:
            width (int): width of rectangle, initialized by constructor
            height (int): height of rectangle, initialized by constructor
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
        The function returns the width attribute of an object.
        :return: The width of the object.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        :param value: The parameter "value" represents the width
        value that is being passed to the method
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        The height function returns the width of an object.
        :return: The width of the object.
        """
        return self.__width

    @height.setter
    def height(self, value):
        """
        :param value: The parameter "value" represents the height
        value that is being passed to the method
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
