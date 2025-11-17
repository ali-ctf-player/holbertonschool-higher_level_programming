#!/usr/bin/python3

def replace_in_list(my_list, idx, new_element):
    if idx >= len(my_list) or idx < 0:
        return my_list
    else:
        my_list[idx] = new_element
        return my_list
