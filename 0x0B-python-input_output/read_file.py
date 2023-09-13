#!/usr/bin/python3
"""
this function reads a text file using the utf8 encoding
Prints the contents to stdout

"""
def read_file(filename=""):
    """ Uses the with statement """
    with open('filename', encoding="utf-8") as file
        for line in file:
            print(line, end="")
