#!/usr/bin/python3
for i in range(97, 123):
    convertAsciiToLetter = chr(i)
    numToAlpha = "" + convertAsciiToLetter
    print("{}".format(numToAlpha), end='')
