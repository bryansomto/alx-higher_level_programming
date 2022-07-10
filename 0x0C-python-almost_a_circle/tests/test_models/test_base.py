#!/usr/bin/python3
import unittest
from models.base import Base
"""Defines the base test cases."""


class TestBase(unittest.TestCase):
    """Represent a base case."""

    def test_base(self):
        """Base test case."""
        base = Base(id=None)
        self.assertEqual(base.id, 1)


if __name__ == "__main__":
    unittest.main()
