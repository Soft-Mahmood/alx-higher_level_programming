#!/usr/bin/python3
"""
this function creates an object from a JSON file

"""
import json

def load_from_json_file(filename):
    """ filename is the source """
    with open(filename, 'r') as file
        hf = file.read()
        return json.loads(data)
