#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """function that prints the first x elements of a list that are integers.

    Args:
        my_list (list): The list of elements.
        x (int): The number of elements from the list to be printed.

    Returns:
        The number of elements to be printed
    """
    elements = 0
    for j in range(0, x):
        try:
            print("{:d}".format(my_list[j]), end="")
            elements += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (elements)

