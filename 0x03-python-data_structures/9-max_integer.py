#!/usr/bin/python3
#9-max_integer.py

def max_integer(my_list=[]):
    """function that finds the biggest integer of a list."""
    if len(my_list) == 0:
            return (None)
        
        max_int = my_list[0]
        for j in range(len(my_list)):
            if my_list[j] > max_int:
                max_int = my_list[j]
                return (max_int)
