#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    else:
        list_t = my_list.copy()
        list_t.sort()
        return list_t[-1]
