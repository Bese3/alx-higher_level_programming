#!/usr/bin/python3

# The Square class represents a square shape.
class Square:
    def __init__(self , size=0):
        """
        The above code defines a class with methods to calculate the area of a square, set and get the
        size of the square, and print a square of a given size.
        
        :param size: The "size" parameter represents the size of a square. It is an optional parameter
        with a default value of 0. The size must be an integer and greater than or equal to 0, defaults
        to 0 (optional)
        """
        if type(size) is  not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        return (self.__size)**2
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self , value):
        if type(value) is  not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value
    def my_print(self):
        if self.__size == None:
            print()
            return self.__size
        for i in range(self.__size):
            for j in range(self.__size):
                print("#" ,end = "")
            print()