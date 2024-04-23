#!/usr/bin/python3

"""function"""
import json


def load_from_json_file(filename):
    """file"""
    with open(filename) as fle:
        return json.load(fle)
