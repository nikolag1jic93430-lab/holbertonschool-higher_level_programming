#!/usr/bin/python3
"""
This module defines a function that writes an object
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text .

    Args:
        my_obj: The object to serialize.
        filename (str)
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
