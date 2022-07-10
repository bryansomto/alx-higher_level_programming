#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
"""Defines the rectangle model test cases."""


class TestRectangle(unittest.TestCase):
    """Represent a rectangle test case."""

    def test_rectangle(self):
        """Rectangle test case."""
        rec = Rectangle(10, 5, 6, 6, 12)
        self.assertEqual(rec.width, 10)
        self.assertEqual(rec.height, 5)
        self.assertEqual(rec.x, 6)
        self.assertEqual(rec.y, 6)
        self.assertEqual(rec.id, 12)


if __name__ == "__main__":
    unittest.main()
