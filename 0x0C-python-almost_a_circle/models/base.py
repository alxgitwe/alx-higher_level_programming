#!/usr/bin/python3
"""class"""
import csv
from json import dumps, loads


class Base:
    """hierarchy"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)            
