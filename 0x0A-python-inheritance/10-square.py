#!/usr/bin/python3
'''Module for the Rectangle class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A subclass represente the rectangle.'''
    def __init__(self, size):
        '''Constructore.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Methode for area of the square.'''
        return self.__size ** 2
