#!/usr/bin/python3
"""Defines a text file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file (UTF8).

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the end of file.
    Returns:
        The number of characters added.
    """
    with open(filename, mode="a", encoding="UTF-8") as a_file:
        return a_file.write(text)
