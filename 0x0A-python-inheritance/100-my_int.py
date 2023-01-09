#!/usr/bin/python3

"""100-my_int
Contains MyInt, which inherits from standard type int
"""


class MyInt(int):
    """
    Inherits from int and overloads the != and == operators, it swaps them
    """
    def __eq__(self, other):
        return self.real != other

    def __ne__(self, other):
        return self.real == other
