#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    a = 0
    b = None
    for i, j in a_dictionary.items():
        if j > a:
            a = j
            b = i
    return b
