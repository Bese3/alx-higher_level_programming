#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    The function `matrix_divided` takes a matrix and a divisor as input, and returns a new matrix where
    each element is divided by the divisor and rounded to two decimal places.
    
    :param matrix: The matrix parameter is a list of lists representing a matrix. Each inner list
    represents a row in the matrix, and the elements of the inner lists represent the values in each
    row. The matrix can contain integers or floats
    :param div: The div parameter is the number by which each element in the matrix will be divided
    :return: a new matrix that is the result of dividing each element of the input matrix by the input
    divisor.
    """
    for rows in matrix:
        for i in rows:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    common_len = len(matrix[0])
    for rows in matrix:
        if len(rows) != common_len:
            raise TypeError("Each row of the matrix must have the same size")
    
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_list = []
    for rows in matrix:
        new_list.append([])
        for i in rows:
            new_list[-1].append(round(i / div , 2))
    
    return new_list