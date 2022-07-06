#!/usr/bin/python3
"""Defines a JSON file reading function."""
import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file."""
    with open(filename) as a_file:
        json.load(a_file)
