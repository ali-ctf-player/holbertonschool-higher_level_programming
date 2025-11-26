#!/usr/bin/python3
import pickle

def serialize_and_save_to_file(data, filename):
    """Serializes data and saves it to a file"""
    try:
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
    except (TypeError, pickle.PickleError, AttributeError):
        raise TypeError("Object is not serializable")

def load_and_deserialize(filename):
    """Loads and deserializes data from a file"""
    with open(filename, 'rb') as file:
        return pickle.load(file)
