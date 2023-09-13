#!/usr/bin/python3
"""
the function writes an object to a ext file

"""
import json
def save_to_json_file(my_obj, filename):
    """
    my_obj is the object
    filename is the filename
    """
    with open(filename, 'w') as file:
        json.dumps(my_obj, file)
