#!/usr/bin/python3
"""It is doc string"""


def write_file(filename="", text=''):
    """It is doc string"""
    with open(filename, 'w', encoding="utf-8") as f:
        content = str(text)
        f.write(content)
