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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size


    def area(self):
        """function that calculates area of the square"""

        return self.__size * self.__size
