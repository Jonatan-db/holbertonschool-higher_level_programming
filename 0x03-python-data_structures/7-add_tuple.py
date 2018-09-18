#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    castedA = list(tuple_a)
    castedB = list(tuple_b)
    castedA.append(0) if len(castedA) is 1 else castedA.extend([0, 0])
    castedB.append(0) if len(castedB) is 1 else castedB.extend([0, 0])
    return (castedA[0] + castedB[0], castedA[1] + castedB[1])
