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
        width and height are initialized here.
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
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

    def area(self):
        """
        Calculates the area of the Rectangle
        Returns:
            area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the Rectangle
        Returns:
            perimeter of the Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @property
    def width(self):
        """Get private attribute width
        Returns:
            The attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the private attribute width to value, or raises an exception
        if value doesn't meet the requirements
        Args:
            value (int): the new value of width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get private attribute height
        Returns:
            The attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the private attribute height to value, or raises an exception
        if value doesn't meet the requirements
        Args:
            value (int): the new value of height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """
        The function returns a string representation of a rectangle made up of
        '#' characters, with the height and width specified by the object's
        attributes.
        """
        new_string = ""
        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                new_string += '#'
            new_string += '\n' if i != self.__height - 1 else ""
        return new_string

    def __repr__(self):
        return "Rectangle({} , {})".format(self.__width, self.__height)

    def __del__(self):
        del self
        print("Bye rectangle...")
