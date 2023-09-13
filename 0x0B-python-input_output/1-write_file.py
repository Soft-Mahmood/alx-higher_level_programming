#!/usr/bin/python3
"""
This function writes a string to a text file
Returns the number of characters written

"""
def write_file(filename="", text=""):
    """ Text is the text string to insert. """
    with open(filename, 'w') as file:
        wr = file.write(text)
    return wr
