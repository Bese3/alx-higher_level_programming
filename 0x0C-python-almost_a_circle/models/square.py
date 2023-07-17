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

    @property
    def size(self):
        """
        The size function returns the width of an object.
        :return: The width of the object.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        The function sets the width and height of
        an object to a given value, but raises errors if the
        value is not an integer or is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for i, j in kwargs.items():
                setattr(self, i, j)

    def to_dictionary(self):
        """
        The function `to_dictionary` returns
        a dictionary with the attributes of an object.
        """
        first = {'id': self.id, 'x': self.x, 'size': self.size}
        second = {'y': self.y}
        first.update(second)
        return first

    def __str__(self):
        """
        The function returns a string representation
        of a Rectangle object, including its id,coordinates,
        width, and height.
        """
        string = F"[Square] ({self.id}) {self.x}/{self.y}" + \
            F" - {self.width}"
        return string
