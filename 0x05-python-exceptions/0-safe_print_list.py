#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """function that prints x elememts of a list.

    Args:
        my_list (list): The list that has elements.
        x (int): The number of elements from list to printed.

    Returns:
        The number of elements
    """
    elements = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
            elements += 1
        except IndexError:
            break
    print("")
    return (elements)
