#!/usr/bin/python3
'''Modules for MyList class.'''


class MyList(list):
    '''Custome MyList class.'''
    def print_sorted(self):
        '''Methode for printing sorted list.'''
        print(sorted(self))
