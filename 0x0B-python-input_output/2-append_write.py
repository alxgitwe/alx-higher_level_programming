#!/usr/bin/python3

"""function"""


def append_write(filename="", text=""):
    """file"""
    with open(filename, "a", encoding="utf-8") as fle:
        return fle.write(text)
