#!/usr/bin/python3
"""
The `print(new_list)` statement at the end
of the code is printing the resulting matrix after
multiplying `m_a` and `m_b`.
"""


def matrix_mul(m_a, m_b):
    """
    The function `matrix_mul` takes two matrices as
    input and returns their product if they can be
    multiplied, otherwise it raises appropriate errors.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for i in m_a:
        if type(i) != list:
            raise TypeError("m_a must be a list of lists")
    for j in m_b:
        if type(j) != list:
            raise TypeError("m_b must be a list of lists")
    for j in m_b:
        if j == []:
            raise ValueError("m_b can't be empty")
    for i in m_a:
        if i == []:
            raise ValueError("m_a can't be empty")
    for i in m_a:
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("m_b should contain only integers or floats")
    first = len(m_a[0])
    second = len(m_b[0])
    for i in m_a:
        if len(i) != first:
            raise TypeError("each row of m_a must be of the same size")
    for j in m_a:
        if len(j) != second:
            raise TypeError("each row of m_b must be of the same size")
    third = len(m_b)
    if first != third:
        raise ValueError("m_a and m_b can't be multiplied")
    new_list = []
    for rows_a in m_a:
        coulumn_iterate = 0
        new_list.append([])
        while coulumn_iterate < len(m_b[0]):
            result = 0
            row_iterate = 0
            for rows_b in m_b:
                result += rows_a[row_iterate] * rows_b[coulumn_iterate]
                row_iterate += 1
            new_list[-1].append(result)
            coulumn_iterate += 1
    return new_list
