#!/usr/bin/python3

""" This is module for Task 2 """


class Square:
    """Square class with __init__ function.
    Handles ValueError, TypeError for size"""

    def __init__(self, size=0):
        """
        initialization function for Square class

        Args:
            size: The size of the square. Defaults to 0
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """function that calculates area of the square"""

        return self.__size * self.__size

    def my_print(self):
        """Prints a square with the charactar `#`,
        if size is 0 a blanck line will be printed"""

        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
