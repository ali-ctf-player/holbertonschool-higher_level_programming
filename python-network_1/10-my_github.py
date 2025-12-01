#!/usr/bin/python3
"""It is doc string"""

import requests
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(
        'https://api.github.com/user', auth=(username, password)
        )

    try:
        user_data = response.json()
        user_id = user_data.get('id')

        print(user_id)

    except Exception:
        print(None)
