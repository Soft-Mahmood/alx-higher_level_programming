#!/usr/bin/python3

"""
Module 3-square
Defines class Square with private attribute size and public attrribute area
"""


class Square:
    """
    class Sqaure definition
    Args:
       size(int): size of side of square
    Functions:
        __init__(self, size)
        area(self)
    """
    def __init__(self, size = 0):
        """
        Initialises class Square
        Attributes:
            __size (int): size of side of square
        """
                if type(size) is not int:
                        raise TypeError("Size must be an integer")
                elif size < 0:
                        raise ValueError("Size must be >= 0")
                else:
                        self.__size = size
	def area(self):
	""" 
        Calculates the area of the square
        Returns:
             the area of the current square
        """
            return self.size ** 2
