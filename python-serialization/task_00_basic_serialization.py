#!/usr/bin/python3
"""
This module handles basic JSON 
"""


import json

def serialize_and_save_to_file(data, filename):
    """
    Save a Python dictionary to a file as JSON.

    Args:
        data (dict): Data to serialize.
        filename (str): Name of the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    Load JSON data from a file 

    Args:
        filename (str): Name of the file to read from.

    Returns:
        dict: The deserialized data.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
