#!/usr/bin/python3

"""
Module 1-rectangle
Defines class rectangle with two private attributes width and height
"""


class Rectangle:
    """
    Rectangle is an empty class that defines a rectangle
    Attributes:
        width: the shorter side
        height: the longer side
    """
    def __init__(self, width = 0, height = 0):
        """
        initialises the rectangle
        Attributes:
            width: the shorter side
            height: the longer side
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Gtter for the width """
        return self.__width

    @property
    def height(self):
        """ Getter for the height """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Setter for the width
        Note: 
            Width should be an int
            must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter for the height
        Note:
            Height must be an int
            Must be > 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
