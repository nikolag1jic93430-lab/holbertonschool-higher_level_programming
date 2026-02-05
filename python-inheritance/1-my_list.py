#!/usr/bin/python3
"""Defines an inherited """


class MyList(list):
    """Implements sorted printing """

    def print_sorted(self):
        """Print a list"""
        print(sorted(self))
