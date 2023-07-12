#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []
    new_list = []
    i = 0
    while i < n:
        new_list.append([])
        j = -1
        while j < i:
            new_list[-1].append(1)
            j += 1
        i += 1
    i = 2
    while i < n:
        if i != n:
            j = i - 1
            no_iter = 0
            while no_iter < j:
                no_iter += 1
                new_list[i][i - no_iter] = new_list[i - 1][i - no_iter - 1]\
                    + new_list[i - 1][i - no_iter]
        i += 1
    return new_list
