#!/usr/bin/python3

# The Square class represents a square shape.
class Square:
    def __init__(self , size=0 , position = (0 , 0)):
        """
        The above code defines a class with methods to set and get the size and position of a square,
        calculate its area, and print it.
        
        :param size: The "size" parameter represents the length of one side of a square. It determines
        the size of the square object, defaults to 0 (optional)
        :param position: The "position" parameter is a tuple of two positive integers that represents the
        starting position of the square when printing it. The first element of the tuple represents the
        number of spaces to be printed before each line of the square, and the second element represents
        the number of spaces to be printed before each row
        """
        if type(size) is  not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size
        if position < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self,value):
        if value < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    
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
            for k in range(self.__position[0]):
                print(" ")
            for j in range(self.__size):
                print("#" ,end = "")
            print()