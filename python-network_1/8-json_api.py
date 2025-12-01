#!/usr/bin/python3
"""It is doc string"""

import requests
import sys

if __name__ == "__main__":

    letter = "" if len(sys.argv) == 1 else sys.argv[1]

    data = {"q": letter}

    response = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        json_response = response.json()

        if not json_response:
            print("No result")
        else:
            name = json_response.get('name')
            id = json_response.get('id')

            print(f"[{id}] {name}")

    except Exception as e:
        print("Not a valid JSON")
