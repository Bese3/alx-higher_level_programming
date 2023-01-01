#!/usr/bin/python3

"""2-matrix_divided
Holds the function matrix_divided and used to test the function using
tests/2-matrix_divided.txt
"""


def matrix_divided(matrix, div):
    """
    Divides each number in matrix by div, and returns it as the new matrix.
    If one of the elements in the matrix is not a number (int or float),
    TypeError with message "matrix must be a matrix (list of lists) of
    integers/floats" is raised. If each list inside the matrix doesn't have
    the same length, a TypeError with message "Each row of the matrix must
    have the same size" is raised. If div is not a number, a TypeError
    exception with the message "div must be a number" is raised. If div is
    equal to 0, ZeroDivisionError with message "division by zero" is raised.

    Args:
        matrix (list): 2D list of numbers
        div (int, float): number that'll divide each number in matrix
    Returns:
        A 2D list of numbers, each the quotient of the respective element
        in the argument matrix, with div as the divisor.
    """

    for inner_list in matrix:
        for i in inner_list:
            if type(i) is not int and type(i) is not float or i is None:
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

    len_of_inner_list = len(matrix[0])
    for inner_list in matrix:
        if len(inner_list) != len_of_inner_list:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len_of_inner_list):
            new_matrix[-1].append(round(matrix[i][j] / div, 2))

    return new_matrix
