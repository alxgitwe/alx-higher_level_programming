#!/usr/bin/python3
"""function"""


def say_my_name(first_name, last_name=""):
    """name"""
    if not isinstance(first_name, i):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, i):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
