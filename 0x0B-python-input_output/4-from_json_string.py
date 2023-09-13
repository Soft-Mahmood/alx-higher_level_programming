#!/usr/bin/python3
"""
FUnction returns the object represented by a JSON string


"""
import json
def from_json_string(my_str):
    """ my_str is the json string """
    return json.loads(my_str)
