#!/usr/bin/python3

"""module class"""
from models.base import Base


class Rectangle(Base):
    """class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        """method validating"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
         """Computes area"""
         area = self.width * self.height
         return area

    def display(self):
        """"rectangle"""
        s = '\n' * self.y + \
                (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end="")

    def __str__(self):
        """__str__"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """__update"""
        names = ["id", "width", "height", "x", "y"]
        if args and len(args) != 0:
            for k in range(len(args)):
                setattr(self, names[k], args[k])
        else:
            for h, l in kwargs.items():
                if h in names:
                    setattr(self, h, l)

    def to_dictionary(self):
        """dictionary"""
        return {"id": self.id, "width": self.__width, "height": self.__height, "x": self.__x, "y": self.__y}

