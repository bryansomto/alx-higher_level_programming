#!/usr/bin/python3
"""Defines a base class for all classes in this project."""


class Base:
    """Represents a base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new base method."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
