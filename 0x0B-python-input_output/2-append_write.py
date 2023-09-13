#!/bin/usr/python3
"""
this function appends a string to the end of a text file.
Returns the number of xters

"""
def append_write(filename="", text=""):
    """ if the file doesnt exist, it is created """
    with open(filename, 'a') as file:
        wr = file.write(text)
    return wr
