#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys = []
    if value not in a_dictionary.values():
        return a_dictionary
    else:
        for i in a_dictionary.keys():
            if value == a_dictionary[i]:
                keys.append(i)
        for i in keys:
            del a_dictionary[i]
        return a_dictionary
