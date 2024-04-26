#!/usr/bin/python3
"""class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class"""

    def __init__(self, size, x=0, y=0, id=None):
        """__init__"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """square"""
        return '[{}] ({}) {}/{} - {}'.\
                format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size"""
        return self.width

    @size.setter
    def size(self, value):
        self.height = value
        self.width = value

    def __update(self, id=None, size=None, x=None, y=None):
        """update"""
        if id is not None:
            self.id = id
        elif size is not None:
            self.size = size
        elif x is not None:
            self.x = x
        elif y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """update"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """dictionary"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

