#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
calling BaseGeometry from other module
"""

class Rectangle(BaseGeometry):
    """
      The Rectangle class is a subclass of BaseGeometry
      that represents a rectangle with a given width and
      height, validating that the values are integers.
    """
    def __init__(self, width, height):
        """
        The function initializes an object with a given
         width and height, while also validating that the
         values are integers.
        :param width: The "width" parameter is the
         width of the object or shape. It is used to
         initialize the width attribute of the object
        :param height: The "height" parameter is the height
         of the object or shape being represented. It
         is used to initialize the height attribute of the object
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height