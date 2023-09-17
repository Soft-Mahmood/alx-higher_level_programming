#!/usr/bin/python3
"""
Class square
Inherits from rectangle


"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    class square inherits from rect
    methods:

    """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialising the class """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ getter for the size """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter for the size
        Args:
            value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updates the attributes of square """
        if args != ():
            if len(args) >= 2:
                newargs = args[0:2] + args[1:]
            else:
                newargs = args
            super().update(*newargs)
        else:
            newkwargs = dict()
            for k, v in kwargs.items():
                if k == "size":
                    newkwargs["width"] = v
                    newkwargs["height"] = v
                else:
                    newkwargs[k] = v
            super().update(**newkwargs)

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        ds = super().to_dictionary()
        ds["size"] = ds["height"]
        del ds["height"]
        del ds["width"]
        return ds

