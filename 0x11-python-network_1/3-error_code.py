#!/usr/bin/python3
"""
    script that takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8).
"""
from urllib import request, error
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            body = response.read()
            print(body.encode("UTF-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
