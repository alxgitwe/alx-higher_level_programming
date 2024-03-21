#!/usr/bin/python3

def uniq_add(my_list=[]):
    q = []
    i = 0
    for j in my_list:
        if j not in q:
            i = i + j
            q.append(j)
    return i
