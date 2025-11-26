#!/usr/bin/python3
"""It is doc string"""


def serialize_and_save_to_file(data, filename):
    """It is doc string"""
    import pickle
    try:
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
    except (pickle.PickleError, TypeError) as e:
        raise TypeError()


def load_and_deserialize(filename):
    """It is doc string"""
    import pickle
    with open(filename, 'rb') as file:
        return pickle.loads(file.read())
