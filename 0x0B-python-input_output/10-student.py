#!/usr/bin/python3

"""class"""


class Student:
    """class"""

    def __init__(self, first_name, last_name, age):
        """new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """representation"""
        if (type(attrs) == list and
                all(type(y) == str for y in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__
