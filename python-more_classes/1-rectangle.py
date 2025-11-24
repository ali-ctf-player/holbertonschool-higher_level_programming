#!/usr/bin/python3
"""It is about classes in Python"""


class Rectangle:
    """It is class named Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """It is doc string"""
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @property
    def height(self):
        """It is doc string"""
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        return self.__height
