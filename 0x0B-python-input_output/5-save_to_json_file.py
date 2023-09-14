#!/usr/bin/python3
"""
This function writes an object to a text file
Using JSON representation

"""
import json
def save_to_json_file(my_obj, filename):
    """ my_obj is the object to be added to the file filename """
    with open(filename, 'w') as file
        jso = json,dumps(my_obj)
        file.write(jso)
