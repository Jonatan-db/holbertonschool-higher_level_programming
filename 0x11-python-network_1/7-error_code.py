#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL and
displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    poop = requests.get(sys.argv[1])
    highschoolmusical = poop.status_code
    if highschoolmusical >= 400:
        print("Error code: {}".format(highschoolmusical))
    else:
        print(poop.text)
