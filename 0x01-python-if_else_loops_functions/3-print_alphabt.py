#!/usr/bin/python3
for i in range(97, 123):
    convertAsciiToLetter = chr(i)
    numToAlpha = "" + convertAsciiToLetter
    if i == 101 or i == 113:
        continue
    print("{}".format(numToAlpha), end='')
