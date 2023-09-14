#!/usr/bin/python3
"""
this function reads a textfile
Prints the cotents to stdout

"""
def read_file(filename=""):
    """ filename is the name of the file """
    with open(filename, encoding="uft-8") as file
        for line in file:
            print(line, end="")
