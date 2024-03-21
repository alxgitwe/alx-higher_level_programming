#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    q = {}
    for i, j in a_dictionary.items():
        q.update({i: (j * 2)})
    return q
