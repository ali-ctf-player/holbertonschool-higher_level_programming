#!/usr/bin/python3

def element_at(mylist, idx):
    if idx >= len(mylist):
        return None
    else:
        if idx < 0:
            return None
        else:
            return mylist[idx]
