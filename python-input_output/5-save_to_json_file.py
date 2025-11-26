#!/usr/bin/python3
"""It is doc string"""


def save_to_json_file(my_obj, filename):
    """It is doc string"""
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
