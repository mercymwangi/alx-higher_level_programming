#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_ord = list(a_dictionary.keys())
    dict_ord.sort()
    for j in dict_ord:

        print("{}: {}".format(j, a_dictionary.get(j)))

