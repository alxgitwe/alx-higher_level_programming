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
    
    @staticmethod
    def from_json_string(json_string):
        """from_json_string"""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file"""
        if list_objs is not None:
            list_objs = [x.to_dictionary() for x in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as fle:
            fle.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """create"""
        from models.square import Square
        from models.rectangle import Rectangle
        if cls is Rectangle:
            i = Rectangle(1, 1)
        elif cls is Square:
            i = Square(1)
        else:
            i = None
        i.update(**dictionary)
        return i

    @classmethod
    def load_from_file(cls):
        """load_from_file"""
        from os import path
        fle = "{}.json".format(cls.__name__)
        if not path.isfile(fle):
            return []
        with open(fle, "r", encoding="utf-8") as f:
            return [cls.create(**i) for i in cls.from_json_string(f.read())]
