#!/usr/bin/python3
'''Module for is_same_class methode.'''


def is_same_class(obj, a_class):
    '''Determine if an objecte is exactly an instance of the class.'''
    return type(obj) == a_class
