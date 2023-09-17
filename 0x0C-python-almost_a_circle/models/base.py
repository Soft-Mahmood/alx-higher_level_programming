#!/usr/bin/python3
"""
This module base
Has the base class for other classes in this project

"""
class Base:
    """
    This is the base class
    This will manage the id attribute.

    Attributes:
        id(str): id of the class

    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        If id is none, assign the public instance attribute.
        id is an integer.
        If id is not none, increment __nb_onjects and assign the new value to the public instance attribute id

        """
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
