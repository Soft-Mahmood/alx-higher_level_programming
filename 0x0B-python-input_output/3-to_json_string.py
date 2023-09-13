#!/usr/bin/python3
"""
this function returns the JSON representation of an object


"""
import json
def to_json_string(my_obj):
    """ my_obj is the object to be serialised """
    du = json.dumps(my_obj)
    return du
