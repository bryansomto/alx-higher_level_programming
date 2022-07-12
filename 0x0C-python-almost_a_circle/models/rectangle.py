#!/usr/bin/python3
"""Defines a base class for all classes in this project."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    @property
    def width(self):
        """width getter function."""
        return self.__width

    @property
    def height(self):
        """height getter function."""
        return self.__height

    @property
    def x(self):
        """x getter function."""
        return self.__x

    @property
    def y(self):
        """y getter function."""
        return self.__y

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new rectangle method.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.

        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = super().__init__(id)

    def area(self):
        """Defines the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for i in range(self.width)]
            print("")

        def __str__(self):
            """Return the print() and str() representation of the Rectangle."""
            return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                            self.x, self.y,
                                                            self.width, self.height)
