#!/usr/bin/python3

def replace_in_list(my_list, idx, new_element):
    if idx >= len(my_list):
        return my_list
    else:
        if idx < 0:
            return my_list
        else:
            my_list[idx] = new_element
            return my_list

print(replace_in_list([1,2,3],0,2))
