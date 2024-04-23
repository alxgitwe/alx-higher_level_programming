#!/usr/bin/python3

"""class"""


class Student:
    """student"""

    def __init__(self, first_name, last_name, age):
        """Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """representation"""
        if (type(attrs) == list and
                all(type(x) == str for x in attrs)):
            return {y: getattr(self, y) for y in attrs if hasattr(self, y)}
        return self.__dict__

    def reload_from_json(self, json):
        """replace"""
        for i, j in json.items():
            setattr(self, i, j)
