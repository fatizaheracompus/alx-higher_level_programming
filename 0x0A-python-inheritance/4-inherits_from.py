#!/usr/bin/python3
'''Module for inherits_from methode.'''


def inherits_from(obj, a_class):
    '''Determine if an object is  true subclass of the class.'''
    return isinstance(obj, a_class) and type(obj) != a_class
