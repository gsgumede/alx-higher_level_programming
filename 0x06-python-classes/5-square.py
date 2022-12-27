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
            raise ValueError("size must be >=0")
        self.__size = size

    @property
    def size(self):
        """Get/set a size attribute"""
        return (self.size)

    @size.setter
    def size(self, value):
        """Set a size attribute"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with character #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
