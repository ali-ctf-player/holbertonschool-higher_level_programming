#!/usr/bin/python3
"""It is doc string"""


def append_write(filename="", text=''):
    """It is doc string"""
    with open(filename, 'a', encoding="utf-8") as f:
        content = str(text)
        f.write(content)
        return len(content)
