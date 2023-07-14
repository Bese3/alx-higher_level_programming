#!/usr/bin/python3
"""importing everything"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        The above function is a constructor that initializes
        an object with a given size, position, and optional id.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        The function returns a string representation
        of a Rectangle object, including its id,coordinates,
        width, and height.
        """
        string = F"[Square] ({self.id}) {self.x}/{self.y}" + \
            F" - {self.width}/{self.height}"
        return string
