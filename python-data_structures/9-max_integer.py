#!/usr/bin/python3

def max_integer(my_list):
    result = my_list[0]
    if len(my_list) == 0:
        result = None
    else:
        for i in my_list:
            if i > result:
                result = i
    return result
