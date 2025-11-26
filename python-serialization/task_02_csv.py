#!/usr/bin/python3
"""It is doc string"""
import json
import csv


def convert_csv_to_json(filename):

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            csv_content = csv.DictReader(file)
            data = list(csv_content)

        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(data, file)

        return True

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return False

    except Exception as e:
        print(f"Error during conversion: {e}")
        return False
