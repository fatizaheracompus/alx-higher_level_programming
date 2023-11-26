#!/usr/bin/python3
'''Module of the  Rectangle class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A subclass represent the rectangle.'''
    def __init__(self, size):
        '''Constructore.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Methode for area of the square.'''
        return self.__size ** 2

    def __str__(self):
        '''Returns string represent this square.'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
