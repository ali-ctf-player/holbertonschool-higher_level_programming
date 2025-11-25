#!/usr/bin/python3
"""
    Rectangle class that inherits from BaseGeometry
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Rectangle class that inherits from BaseGeometry
    """
    def __init__(self, size):

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Rectangle class
        """
        return self.__size * self.__size
