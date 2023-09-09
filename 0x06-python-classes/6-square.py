#!/usr/bin/python3

"""The Square class represents a square shape."""


class Square:
    """square class"""

    def __init__(self, size=0, position=(0, 0)):
        """
        The above code defines a class with methods
        to set and get the size and position of a square,
        calculate its area, and print it.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size
        if position < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def position(self):
        """
        The function returns the value of the
        private variable __position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        The function sets the position attribute of an object
        to the given value, but raises an error if
        the value is negative.
        """
        if value < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
