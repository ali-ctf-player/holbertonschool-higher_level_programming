#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    temp = []
    for i in a_dictionary.keys():
        temp.append(i)
    temp.sort()
    for i in temp:
        print("{}: {}".format(i, a_dictionary[i]))
