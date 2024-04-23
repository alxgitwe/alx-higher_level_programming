#!/usr/bin/python3
"""class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """rectangle"""
    def __init__(self, size):
        """rectangle"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area"""
        return self.__size * self.__size
