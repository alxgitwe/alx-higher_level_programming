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

