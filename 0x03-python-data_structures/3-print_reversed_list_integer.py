#!/usr/bin/python3
#3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """function that prints all intergers in reverse order."""
    if isinstance(my_list, list):
        my_list.reverse()
        for j in my_list:
            print("{:d}".format(j))
