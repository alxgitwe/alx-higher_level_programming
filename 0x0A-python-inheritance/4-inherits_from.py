#!/usr/bin/python3
"""function"""


def inherits_from(obj, a_class):
    """object"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
