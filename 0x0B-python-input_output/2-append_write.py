#!/usr/bin/python3
"""
This function appends a string t the end of the file
Returns the number of characters added

"""
def append_write(filename="", text=""):
    """ text is the string to append """
    with open(filename, 'a') as file
        app = file.write(text)
    return app
