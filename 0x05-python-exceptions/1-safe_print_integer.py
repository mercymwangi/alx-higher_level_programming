#!/usr/bin/python3


def safe_print_integer(value):
    """function that prints an integer with "{:d}".format().

    Args:
        value (int): The integer to be printed.

    Returns:
        True- if a value has been correctly printed.
        Otherwise - false.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
