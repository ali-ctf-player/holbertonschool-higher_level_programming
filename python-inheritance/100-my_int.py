#!/usr/bin/python3
"""Rectangle"""


class MyInt(int):
    """Rectangle"""

    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
