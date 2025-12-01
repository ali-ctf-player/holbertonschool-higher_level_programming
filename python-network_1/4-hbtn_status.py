#!/usr/bin/python3
"""It is doc string"""

import requests

response = requests.get("https://intranet.hbtn.io/status")

print("Body response:")
print(f"\t- type: {type(response.text)}")
print(f"\t- content: {response.text}")
