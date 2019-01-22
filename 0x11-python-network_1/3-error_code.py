#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import URLError, HTTPError

import sys

if __name__ == "__main__":
    try:
        with urlopen(sys.argv[1]) as request:
            print(request.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
