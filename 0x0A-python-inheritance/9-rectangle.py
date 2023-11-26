#!/usr/bin/python3
'''Module for the Rectangle class.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A the subclass representing of the rectangle.'''
    def __init__(self, width, height):
        '''Constructore.'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Methode which returns area of the rectangle.'''
        return self.__width * self.__height

    def __str__(self):
        '''String representation methode.'''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
