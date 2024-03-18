#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in range(len(matrix)):
        if len(matrix[i]) == 0:
            print()
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]),end="\n" if j is len(matrix[i]) - 1 else " ")
