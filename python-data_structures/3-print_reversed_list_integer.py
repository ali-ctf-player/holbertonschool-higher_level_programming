#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    rev_list = []
    for i in range(1, len(my_list) + 1):
        rev_list.append(my_list[-i])
    for i in rev_list:
        print("{:d}".format(i))
