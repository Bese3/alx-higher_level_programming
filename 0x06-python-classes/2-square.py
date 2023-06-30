#!/usr/bin/python3

# The Square class represents a square shape.
class Square:
     
     def __init__(self , size = 0):
        """
        The function initializes an object with a given size, raising errors if the size is not an
        integer or if it is less than 0.
        
        :param size: The `size` parameter is used to initialize the size of an object. It is an
        optional parameter with a default value of 0. The `__init__` method is a special method in
        Python classes that is called when an object is created. In this case, it is used to
        initialize, defaults to 0 (optional)
        """
       
        if not isinstance(size , int):
            raise TypeError("size must be an integer")
        if size < 0 :
            raise ValueError("size must be >= 0")
        
        self.__size = size

    