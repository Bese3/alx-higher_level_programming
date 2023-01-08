#!/usr/bin/python3
'''Module 6-peak
Contains function find_peak
'''


def find_peak(list_of_integers):
    '''Finds the biggest number in list_of_integers
    and returns it. If the list is empty, None is returned.
    '''
    if len(list_of_integers) == 0:
        return None
    return sorted(list_of_integers)[-1]
