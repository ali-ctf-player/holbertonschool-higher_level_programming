#!/usr/bin/python3
"""it is doc string"""


def load_from_json_file(filename):
    """It is doc string"""
    import json

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        content = str(content)
        return json.loads(content)
