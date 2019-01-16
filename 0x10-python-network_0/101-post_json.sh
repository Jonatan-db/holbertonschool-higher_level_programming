#!/bin/bash
# sends a JSON POST request to a URL and the reponse
curl -sH "Content-Type: application/json" -X POST --data @"$2" "$1"
