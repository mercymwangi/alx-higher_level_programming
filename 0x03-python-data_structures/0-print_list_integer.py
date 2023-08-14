#!/usr/bin/python3
#o-print_list_interger.py

def print_list_integer(my_list=[]):

    """print a list of all intergers."""
    for j in range(len(my_list)):
        print("{:d}".format(my_list[j]))
