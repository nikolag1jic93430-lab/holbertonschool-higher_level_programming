#!/usr/bin/python3
""" Abstract class Animal """


from abc import ABC, abstractmethod


class Animal(ABC):
    """class Animal """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """class Dog """
    def sound(self):
        return ("Bark")


class Cat(Animal):
    """class Cat"""
    def sound(self):
        return ("Meow")
