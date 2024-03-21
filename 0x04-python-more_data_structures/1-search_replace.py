#!/usr/bin/python3
def search_replace(my_list, search, replace):
    q = []
    for i in my_list:
        if i == search:
            q.append(replace)
        else:
            q.append(i)
    return q
