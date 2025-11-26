#!/usr/bin/python3
"""It is doc string"""


def read_file(filename=""):
    """It is doc string"""
    with open(filename, 'r', encoding="utf-8") as f:
        content = f.read()
        print(content, end='')
