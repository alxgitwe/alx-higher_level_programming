#!/usr/bin/python3

"""function"""


def write_file(filename="", text=""):
    """file"""
    with open(filename, "w", encoding="utf-8") as fle:
        return fle.write(text)
