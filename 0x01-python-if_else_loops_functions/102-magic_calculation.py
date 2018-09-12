#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:#loadfast a and b compare <
        return (c)#load fast c return
    if c > b:#loadfast b and b compare >
        return (a + b)#loadfast a, b, binary add, return
    return (a * b - c)#loadfast a, b, multiple, load c, binary sub, return
#run python3
#import dis
#copy paste this code into python3 interface. enter enter.
#dis.dis(magic_calculation)
