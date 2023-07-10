#!/usr/bin/python3
"""
The class `MyList` is a subclass of `list`
that adds a method `print_sorted` to print a sorted
list
"""


class MyList(list):
    def print_sorted(self):
        """
        The function takes a list, creates a new sorted list,
        and then prints the sorted list.
        """
        new_list = self[:]
        new_list.sort()
        print(new_list)
        return new_list
