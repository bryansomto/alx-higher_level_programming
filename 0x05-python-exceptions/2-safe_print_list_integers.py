#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list and only integers.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The real number of integers printed
    """
    elements = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            elements += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (elements)
