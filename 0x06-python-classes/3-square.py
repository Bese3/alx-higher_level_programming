#!/usr/bin/python3
""" The Square class represents a square shape."""


class Square:
    """sqaure class"""

    def __init__(self, size=0):
        """
        The above function is a class constructor that
        initializes an object with a given size and
        calculates the area of the object.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        The above function calculates the area of a square.
        :return: The area of a square with side length equal
        to the value of the private attribute
        `__size`.
        """
        return (self.__size)**2
