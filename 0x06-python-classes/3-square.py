#!/usr/bin/python3
"""Define a square class"""


class Square:
    """Represent a square class"""

    def __init__(self, size):
        """Initialization

        Args:
        size (int): size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=o")
        self.__size = size

    def area(self):
        """Return Area of the square"""
        return (self.__size * self.__size)
