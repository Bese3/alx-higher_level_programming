#!/usr/bin/python3


"""
  rectangle that computes width and height
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        special method for a class
        """
        self.__height = height
        self.__width = width

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
