#!/usr/bin/python3
'''Module for the BaseGeometry class.'''


class BaseGeometry:
    '''A the BaseGeometry class.'''
    def area(self):
        '''Methode to calcul this area.'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Methode for validate the value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
