#!/usr/bin/python3

"""10-square
Contains class Square inheriting from Rectangle
"""

__import__('sys').path.insert(1, '../')
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class defining a square from the Rectangle class"""

    def __init__(self, size):
        """Initialize values here"""
        self.integer_validator("size", size)
        super().__init__(size, size)
