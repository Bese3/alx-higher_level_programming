#!/usr/bin/python3

"""The Square class represents a square shape."""


class Square:
    """square class"""

    def __init__(self, size=0):
        """
        The above code defines a class with methods
        to calculate the area of a square, set and get the
        size of the square, and print a square of a given size.
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
        """
        return (self.__size)**2

    @property
    def size(self):
        """
        The function returns the size of an object.
        :return: The size of the object.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        The function sets the size attribute of an object
        to a given value, but raises an error if the
        value is not an integer or is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        The function prints a square of "#" characters
        with a size determined by the value of the
        "__size" attribute.
        """
        if self.__size is None:
            print()
            return self.__size
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
