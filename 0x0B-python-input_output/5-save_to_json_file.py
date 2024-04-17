#!/usr/bin/python3

"""function"""
import json


def save_to_json_file(my_obj, filename):
    """representation"""
    with open(filename, "w") as fle:
        json.dump(my_obj, fle)
