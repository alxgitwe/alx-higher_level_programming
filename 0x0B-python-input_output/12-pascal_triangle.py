#!/usr/bin/python3
"""function"""


def pascal_triangle(n):
    """Return"""
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]

    x = [[1]]
    for y in range(n-1):
        x.append([a+b for a, b
                         in zip([0] + x[-1], x[-1] + [0])])
    return x
