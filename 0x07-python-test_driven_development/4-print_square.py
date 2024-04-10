#!/usr/bin/python3
"""function"""


def print_square(size):
    """square"""
    if not isinstance(size, i):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        [print("#", end="") for y in range(size)]
        print("")
