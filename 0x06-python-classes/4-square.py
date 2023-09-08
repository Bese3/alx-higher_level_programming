#!usr/bin/python3

# The Square class represents a square shape.
class Square:
    def __init__(self , size=0):
        """
        The above code defines a class with a constructor
        that initializes a size attribute, a method to
        calculate the area of a square, and getter and
        setter methods for the size attribute.
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
