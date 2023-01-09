#!/usr/bin/python3

"""12-pascal_triangle
Contains function pascal_triangle
"""


def pascal_triangle(n):
    """Returns a list of integers representing the Pascal's triangle of n"""

    if n <= 0:
        return []

    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]

    pt_list = [[1], [1, 1]]

    for i in range(n - 2):
        pt_list.append([1])

        for j in range(len(pt_list[-2])):
            pt_list[-1].append(pt_list[-2][j] + pt_list[-2][j + 1])

            if j + 2 == len(pt_list[-2]):
                break
        pt_list[-1].append(1)

    return pt_list
