#!/usr/bin/python3
"""
this function deserialises a JSON string

"""
import json
def from_json_string(my_str):
    """ my_str is the string to be deserialised """
    return json.loads(my_str)
