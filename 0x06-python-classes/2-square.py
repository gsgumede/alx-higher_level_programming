#!/usr/bin/python3
"""Define a square class"""


class Square:
    """Represent a square class"""

    def __init__(self, size=0):
        """Initialization

        Args:
        size (int): size of the square
        """
        if type(size) != int:
                raise TypeError("size must be an integer")
        if size < 0:
             raise ValueError("size must be >= 0")
        self.__size = size
