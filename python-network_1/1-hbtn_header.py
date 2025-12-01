#!/usr/bin/python3

import sys
import urllib.request

if __name__ == "__main__":
    url = urllib.request.Request(sys.argv[1])

    with urllib.request.urlopen(url) as page:
        headers = page.headers

        request_id = headers['X-Request-Id']
        print(request_id)
