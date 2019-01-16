#!/bin/bash
# script that sends a request to a URL and displays argument
curl -so /dev/null -w "%{http_code}" "$1"
