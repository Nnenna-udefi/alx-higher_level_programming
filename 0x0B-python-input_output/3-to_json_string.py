#!/usr/bin/python3
"""DEfines a object(String) to json function"""
import json


def to_json_string(my_obj):
    """the JSON representation of an object (string)"""
    return json.dumps(my_obj)
