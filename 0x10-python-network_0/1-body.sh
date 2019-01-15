#!/bin/bash
# Bash script that takes in a URL, sends a GET request and posts the reponse
wget -qO- "$1"
