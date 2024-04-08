#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    """rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Rectangle"""
        type(self).number_of_instances += 1
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
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """representation Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        recta = []
        for x in range(self.__height):
            [recta.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                recta.append("\n")
        return ("".join(recta))

    def __repr__(self):
        """representation Rectangle"""
        recta = "Rectangle(" + str(self.__width)
        recta += ", " + str(self.__height) + ")"
        return (recta)

    def __del__(self):
        """message Rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
