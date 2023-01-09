#!/usr/bin/python3

"""7-base_geometry
Contains class BaseGeometry
"""

__import__('sys').path.insert(1, '../')
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Empty class with just one method
    """
    def __init__(self, width, height):
        """Initialize the object's values"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates the area of the Rectangle
        Returns:
            area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
