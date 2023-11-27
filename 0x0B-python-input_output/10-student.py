#!/usr/bin/python3
"""Function define the class Student."""


class Student:
    """Representation the student."""

    def __init__(self, first_name, last_name, age):
        """Initialization the new Student.

        Args:
            first_name (str): The firste names of  student.
            last_name (str): The laste names of student.
            age (int): The ages of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get  dictionary representation of  Student.

        If attrs is list of strings, representation only thise attributes
        includ in liste.

        Args:
            attrs (list): (Optional) The attribute to representation.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
