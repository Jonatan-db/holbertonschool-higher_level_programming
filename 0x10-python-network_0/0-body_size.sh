#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the bytes
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
