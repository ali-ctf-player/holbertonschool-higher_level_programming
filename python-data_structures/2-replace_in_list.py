#!/usr/bin/python3

def replace_in_list(my_list, idx, new_element):
    if idx > len(my_list):
        return None
    else:
        if idx < 0:
            return None
        else:
            my_list[idx] = new_element
