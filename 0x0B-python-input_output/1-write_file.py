#!/usr/bin/python3
"""
This function writes a string to a textfile
Returns the number of characters written

"""
def write_file(filename="", text=""):
    """ text is the text to be added to the file filename """
    with open(filename, 'w') as file
        writ = file.write(text)
    return writ
