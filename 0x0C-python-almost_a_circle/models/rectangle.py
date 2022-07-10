#!/usr/bin/python3
"""Defines a base class for all classes in this project."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle that inherits the base class."""

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @property
    def height(self):
        """Get/set the width of the Rectangle."""
        return self.__height

    @property
    def x(self):
        """Get/set the width of the Rectangle."""
        return self.__x

    @property
    def y(self):
        """Get/set the width of the Rectangle."""
        return self.__y

    @width.setter
    def width(self, value):
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__id = super().__init__(id)
