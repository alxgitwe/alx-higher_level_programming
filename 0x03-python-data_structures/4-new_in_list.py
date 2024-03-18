#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    list_t = my_list.copy()
    list_t[idx] = element
    return list_t
