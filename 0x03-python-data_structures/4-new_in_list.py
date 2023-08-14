#!/usr/bin/python3
#4-new_in_list.py

def new_in_list(my_list, idx, element):
    """function that replaces an element in a copied list."""

    if idx < 0 or idx > (len(my_list) -1):
        return (my_list)

    new_list = [j for j in my_list]
    new_list[idx] = element 
    return (new_list)
