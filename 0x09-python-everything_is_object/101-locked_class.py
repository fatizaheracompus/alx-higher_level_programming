#!/usr/bin/python3
"""function define a locked class."""


class LockedClass:
    """
    Prevent  user from instantiating new LockedClass attribute
    for anything  attribute called 'first_name'.
    """

    __slots__ = ["first_name"]
