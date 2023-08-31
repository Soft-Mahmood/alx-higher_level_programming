#!/usr/bin/python3
class Square:
        """ Class square defines a square by size """
        def __init__(self, size = 0):
                """ initialises size with default 0 
                checks if size has the correct type and value"""
                if type(size) is not int:
                        raise TypeError("Size must be an integer")
                elif size < 0:
                        raise ValueError("Size must be >= 0")
                else:
                        self.__size = size
	def area(self):
	""" returns the area of the current square """
		return self.size ** 2
