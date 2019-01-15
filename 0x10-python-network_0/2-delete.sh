#!/bin/bash
# sends a DELETE request to the URL passed as the first argument and displays
curl -sL -X DELETE "$1"
