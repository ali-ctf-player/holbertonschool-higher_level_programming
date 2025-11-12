#!/usr/bin/python3

def uppercase(a):
    result = ""
    for i in a:
        if ord(i) >= 97 and i <= 122:
            result += chr(ord(i) - 32)
        else:
            result += i
    print(result)
