#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    sqaure implemetation class
    """
    def __init__(self, size):
        """
        initializing for the square class
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        updating the area method for the square
        """
        return (self.__size)**2
