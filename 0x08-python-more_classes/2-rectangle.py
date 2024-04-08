#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """rectangle."""

    def __init__(self, width=0, height=0):
        """Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area Rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """perimeter Rectangle"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
