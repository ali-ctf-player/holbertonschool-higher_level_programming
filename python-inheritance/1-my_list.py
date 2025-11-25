#!/usr/bin/python3
"""
Module: 1-my_list
Contains class MyList that inherits from list
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order
        Does not modify the original list
        """
        # Create a copy of the list and sort it
        print(sorted(self))
