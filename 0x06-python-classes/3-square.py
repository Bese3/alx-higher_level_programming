#!/usr/bin/python3
# The Square class represents a square shape.
class Square:
    def __init__(self , size=0):
        """
        The above function is a class constructor that initializes an object with a given size and
        calculates the area of the object.
        
        :param size: The "size" parameter is used to specify the size of an object. It is an integer
        value that represents the length of one side of a square, defaults to 0 (optional)
        """
        if type(size) is  not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        return (self.__size)**2