#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) >= 2 else ""
    try:
        request = requests.post(
                  "http://0.0.0.0:5000/search_user", data={"q": q}).json()
        if "id" in request and "name" in request:
            print("[{}] {}".format(request["id"], request["name"]))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
