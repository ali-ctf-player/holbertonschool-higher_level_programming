#!/usr/bin/python3
"""It is doc string"""

import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}

    response = requests.post(url, data=data)

    print(response.text)
