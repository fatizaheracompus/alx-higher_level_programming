#!/usr/bin/python3
"""Function define a class Student."""


class Student:
    """Representation a student."""

    def __init__(self, first_name, last_name, age):
        """Initialization the new Student.

        Args:
            first_name (str): The first name of  student.
            last_name (str): The last name of  student.
            age (int): The age of  student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get the dictionary representation of  Student.

        If attrs is a list of strings, representation only those attributes
        include in the list.

        Args:
            attrs (list): (Optional) The attribute to representation.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attribute of  Student.

        Args:
            json (dict): The key/value pair to replace attribute with.
        """
        for k, v in json.items():
            setattr(self, k, v)
