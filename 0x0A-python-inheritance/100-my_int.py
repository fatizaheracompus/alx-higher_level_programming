#!/usr/bin/python3
"""
Contains the class of the MyInt
"""


class MyInt(int):
    """Rebel version of the integer, perfecte for the opposite day!"""
    def __new__(cls, *args, **kwargs):
        """Create the new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is now !="""
        return int(self) == other
