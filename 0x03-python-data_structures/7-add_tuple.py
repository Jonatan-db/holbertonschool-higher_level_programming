#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    cast = []
    cast.append(int(tuple_a[0]) + int(tuple_b[0]))
    cast.append(int(tuple_b[1]) + int(tuple_b[1]))
    return tuple(cast)
