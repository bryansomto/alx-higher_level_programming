#!/usr/bin/python3
"""Defines a text file-writing function."""


def write_file(filename="", text=""):
    """Writes a string at the end of a text file (UTF8).

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, mode="w", encoding="UTF-8") as a_file:
        return a_file.write(text)
