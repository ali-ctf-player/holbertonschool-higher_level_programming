#!/usr/bin/python3
"""It is doc string"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    values = {"email":email}

    data = urllib.parse.urlencode(values).encode("utf-8")
    req = urllib.request.Request(url,data=data,method="POST")

    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode("utf-8")
    
        print(the_page)

