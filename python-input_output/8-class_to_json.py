#!/usr/bin/python3
"""
Function that returns the dictionary description
"""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure."""
    return obj.__dict__
