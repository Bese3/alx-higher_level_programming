#!/usr/bin/python3
"""
Module that finds a peak in a list of integers
"""
def find_peak(list_of_integers):
    """
    The function "find_peak" takes a list of integers as input
    and returns the largest integer in the
    list.
    :param list_of_integers: A list of integers
    :return: the largest integer in the given list.
    """
    if len(list_of_integers) == 0:
        return
    my_list = list_of_integers[:]
    return sorted(my_list)[-1]