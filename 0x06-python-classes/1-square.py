#!/usr/bin/python3

"""
Module 1-square
Defines a class square with private attribute size

"""


class Square:
    """
    Square class defines a square by size (private)
    Args:
        size: size of the side 
    """
    def __init__(self, size):
    """
    initializes the size object
    Attributes:
        size: size of the side
    """
        self.__size = size
