#!/usr/bin/python3
""" class Square that defines a square """


class Square:

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):  # getter permet de lire une valeur privée
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if isinstance(value, int) and value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
