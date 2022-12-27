#!/usr/bin/python3
"""Define a square class"""


class Square:
    """Represent a square class"""

    def __init__(self, size, position=(0, 0)):
        """Initialization

        Args:
        size (int): size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
        if (type(position) != tuple and
            len(position) == 2 and type(position[0]) == int
            and type(position[1]) == int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def position(self):
        """Get a position attribute"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set position attribute"""
        if (type(value) != tuple(2) and len(value) == 2
            and type(value[0]) == int and type(value[1]) == int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position == value

    @property
    def size(self):
        """Get/set a size attribute"""
        return (self.__size)

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
            if self.__position[1] > 0:
                for k in range(self.__position[0]):
                    print(" ", end="")
            else:
                for k in range(self.__position[0]):
                    print(" ", end="")

            for j in range(self.__size):
                print("#", end="")
            print()
