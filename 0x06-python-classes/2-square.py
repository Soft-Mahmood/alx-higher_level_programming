#!/usr/bin/python3

"""
Module 2-square
Defines clas square with private attribute size

"""


class Square:
    """
    Class square defines a square by size
    Args:
        size: size of the side
    """
    def __init__(self, size = 0):
        """
        initialises size with default 0 
        checks if size has the correct type and value
        
        Attributes:
            __size: size of the side in square
        """
        if type(size) is not int:
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.__size = size
