#!/usr/bin/python3
"""It is doc string"""


class CustomObject:
    """It is doc string"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(
            f"""Name: {self.name}
Age: {self.age}
Is Student: {self.is_student}
            """)

    def serialize(self, filename):
        import pickle
        with open(filename, 'wb') as file:
            file.write(pickle.dumps(self))

    @classmethod
    def deserialize(cls, filename):
        import pickle
        with open(filename, 'rb') as file:
            return pickle.loads(file.read())
