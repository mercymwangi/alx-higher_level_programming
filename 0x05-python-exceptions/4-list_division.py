#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """function that divides element by element 2 lists.

    Args:
        my_list_1 (list): first list.
        my_list_2 (list): second list.
        list_length (int): The length of the list.

    Returns:
        A new list with all the divisions.
    """
    new_list = []
    for j in range(0, list_length):
        try:
            division = my_list_1[j] / my_list_2[j]
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            new_list.append(division)
    return (new_list)

