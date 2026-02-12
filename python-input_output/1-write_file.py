#!/usr/bin/python3
"""
This module writes a string to a text file and returns the number of
characters written.
"""


def write_file(filename="", text=""):
    """
    Write text to a file and return the number of characters written.

    Args:
        filename (str): File name.
        text (str): Text to write.

    Returns:
        int: Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
