#!/usr/bin/python3

def safe_print_list(mylist, x=0):
    count = 0
    try:
        for i in range(x):
            print(mylist[i], end="")
            count += 1
    except IndexError:
        pass
    return count
