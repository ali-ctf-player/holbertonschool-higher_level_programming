#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """A custom list that can print a sorted version"""

    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        print(sorted(self))
