#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        max_key = 0
        max_value = ""
        for i in a_dictionary.keys():
            if max_key < a_dictionary[i]:
                max_key = a_dictionary[i]
                max_value = i
        return max_value
    else:
        return None
