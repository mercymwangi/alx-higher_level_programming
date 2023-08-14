#!/usr/bin/python3
#5-no_c.py

def no_c(my_string):
    """function that removes c and C chars in a string."""
    copy = [j for j in my_string if j != 'c' and j != 'C']
    return ("".join(copy))

