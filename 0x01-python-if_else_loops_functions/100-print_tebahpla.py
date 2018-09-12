#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        convertAsciiToLetter = chr(i)
        numToAlpha = "" + convertAsciiToLetter
        print("{}".format(numToAlpha), end='')
    else:
        convertAsciiToLetter = chr(i - 32)
        numToAlpha = "" + convertAsciiToLetter
        print("{}".format(numToAlpha), end='')
