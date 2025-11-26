#!/usr/bin/python3
"""It is doc string"""
import pickle


class CustomObject:
    """It is doc string"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):

        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            return True
        except Exception as e:
            print(f"Error serializing object: {e}")
            return False

    @classmethod
    def deserialize(cls, filename):

        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            return obj
        except Exception as e:
            print(f"Error deserializing object: {e}")
            return None
