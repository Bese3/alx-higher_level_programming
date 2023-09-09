#!/usr/bin/python3

""" The Square class represents a square shape."""


class Square:
    """square class"""

    def __init__(self, size=0):
        """
        The function initializes an object with a given size
        raising errors if the size is not an
        integer or if it is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
