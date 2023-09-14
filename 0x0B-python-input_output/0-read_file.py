#!/usr/bin/python3
"""
Module 0-read_file
has function that reads a textfile
Prints the cotents to stdout

"""
def read_file(filename=""):
    """
    filename is the name of the file
    Args:
        Filename
    """
    with open(filename, encoding="uft-8") as file
        for line in file:
            print(line, end="")
