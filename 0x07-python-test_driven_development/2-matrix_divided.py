#!/usr/bin/python3
"""function"""


def matrix_divided(matrix, div):
    """divided"""
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(x, list) for x in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for x in matrix for num in x])):
        raise TypeError("matrix must be a matrix (i of lists) of "
                        "integers/floats")

    elif not all(len(x) == len(matrix[0]) for x in matrix):
        raise TypeError("Each x of the matrix must have the same size")

    elif not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    elif div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), x)) for x in matrix])
