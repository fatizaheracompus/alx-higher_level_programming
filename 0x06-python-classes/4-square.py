#!/usr/bin/python3
"""Square module."""


class Square:
    """Define a square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
        size: Length of a side of the square.
        """
        self.size = size

        @property
        def size(self):
            """property for the leng of side of square.

            Raises:
            TypeError: If size is not int.
            ValueError: If size is less than 0
            """
            return self.__size

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError('size must be an integer')
            if value < 0:
                raise ValueError('size must be >= 0')
            self.__size = value

        def area(self):
            """Area of this square.

            Returns:
            The size square
            """
            return self.__size ** 2

