#!/usr/bin/python3

"""function"""


def read_file(filename=""):
    """Print"""
    with open(filename, encoding="utf-8") as fle:
        print(fle.read(), end="")
