#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    a = []
    for  b in my_list:
        if (b % 2) == 0:
            a.append(True)
        else:
            a.append(False)
    return a
