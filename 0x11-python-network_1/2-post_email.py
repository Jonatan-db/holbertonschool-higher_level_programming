#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""
from urllib.request import urlopen
from urllib.parse import urlencode
import sys

if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    email2 = urlencode(email)
    email3 = email2.encode('utf-8')

    with urlopen(sys.argv[1], email3) as r:
        print(r.read().decode('utf-8'))
