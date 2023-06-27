#!/usr/bin/python3

""" This is module for Task 2 """


class Square:
    """Square class with __init__ function.
    Handles ValueError, TypeError for size"""

    def __init__(self, size=0, position=(0, 0)):
        """
        initialization function for Square class

        Args:
            size: The size of the square. Defaults to 0
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Returns the property of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Property setter for position attribute
        Args:
            value (tuple): position of the square
        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("Position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """function that calculates area of the square"""

        return self.__size * self.__size

    def my_print(self):
        """Prints a square with the charactar `#`,
        if size is 0 a blanck line will be printed"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                print("#" * self.__size)
