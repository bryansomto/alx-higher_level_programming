#!/usr/bin/python3

def safe_print_division(a, b):
    """Divides 2 integers and prints the result.

    Args:
        a (int): Integer 1.
        b (int): Integer 2.

    Returns:
        The value of the division, otherwise: None
    """
    try:
        result = a / b
        return("{}".format(result))
    except ZeroDivisionError:
        result = None
        return(result)
    finally:
        print("Inside result: {}".format(result))
