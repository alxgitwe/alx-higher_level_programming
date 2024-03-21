#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    q = []
    for i in matrix:
        j = list(map(lambda a: a**2, i))
        q.append(j)
    return q
