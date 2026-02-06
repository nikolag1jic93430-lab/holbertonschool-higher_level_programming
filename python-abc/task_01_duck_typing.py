#!/usr/bin/python3


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """ Abstract class Shape """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        res = 2 * pi * self.radius
        if res < 0:
            res = -res
        return res


class Rectangle(Shape):
    """ sub class Rectangle"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        res = 2 * (self.width + self.height)
        if res < 0:
            res = -res
        return res


def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
