#!/usr/bin/python3
"""It is doc string of python file"""


def inherits_from(obj, a_class):
    """it is inside of function"""

    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    else:
        return False
