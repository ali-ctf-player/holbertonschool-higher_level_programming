#!/usr/bin/python3
"""It is doc string"""


def append_after(filename="", search_string="", new_string=""):
    """It is doc string"""

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.readlines()

    with open(filename, 'w', encoding='utf-8') as file:
        for line in content:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
