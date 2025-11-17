#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = []
    if idx >= len(my_list) or idx < 0:
        new_list = my_list
    else:
        for i in range(len(my_list)):
            if i == idx:
                new_list.append(element)
            else:
                new_list.append(my_list[i])
    return new_list
