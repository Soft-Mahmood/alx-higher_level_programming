#!/usr/bin/python3
"""
Module rectangl
Contains the class rectangle.
Inherits from Base.

"""
from models.base import Base

class Rectangle(Base):
    """
    Rectangle inherits from Base.

    Attributes:
        id: class id
    """
    def __init__(self, width, height, x = 0, y = 0, id = None):
        """
        Width, height, x, y, are private attributes.

        Args:
            Width: width of the rect
            Height: height of the rect
            x: x
            y: y

        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        getter for the width
        returns width

        """
        return self.__width

    @property
    def height(self):
        """
        getter for the height
        returns height

        """
        return self.__height

    @property
    def x(self):
        """
        getter for the x
        returns x

        """
        return self.__x

    @property
    def y(self):
        """
        getter for the y
        returns y

        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        Setter for the width
        CHecks if value is int, and is not < 0

        Args:
            value

        """
        if type(value) is not int:
            raise TypeError('Width must be an integer')
        if value <=0:
            raise ValueError('Width must be > 0')
        self.__width = value


    @height.setter
    def height(self, value):
        """
        Setter for the height
        CHecks if value is int, and is not < 0

        Args:
            value

        """
        if type(value) is not int:
            raise TypeError('Height must be an integer')
        if value <=0:
            raise ValueError('Height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        """
        Setter for x
        CHecks if value is int, and is not < 0

        Args:
            value

        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value <=0:
            raise ValueError('x must be > 0')
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Setter for y
        CHecks if value is int, and is not < 0

        Args:
            value

        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value <=0:
            raise ValueError('y must be > 0')
        self.__y = value


