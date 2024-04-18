#!/usr/bin/python3
"""class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle"""
    def __init__(self, width, height):
        """rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """rectangle"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
