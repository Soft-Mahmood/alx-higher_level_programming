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

    Methods:
        __init__(self, width, height, x=0, y=0, id=None)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        x(self)
        x(self, value)
        y(self)
        y(self, value)
        area(self)
        display(self)

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

    def area(self):
        """
        Calculates the area of the rect

        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the rectangle with #
        """
        print("\n" * self.__y +
              "\n".join(" " * self.__x + "#" * self.__width
                        for i in range(self.height)))

    def __str__(self):
        """ string respresentation of the object """
        return "[Rectangle] ({}) {}/{} -{}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ updates the instance attributes:
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        """
        count = 0
        if args != ():
            for a in args:
                count += 1
                if count == 1:
                    self.id = a
                if count == 2:
                    self.width = a
                if count == 3:
                    self.height = a
                if count == 4:
                    self.x = a
                if count == 5:
                    self.y = a
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        Retunrs dictionary representation of Rectangle
        """
        r = {}
        r["id"] = self.id
        r["width"] = self.width
        r["height"] = self.height
        r["x"] = self.x
        r["y"] = self.y
        return r
