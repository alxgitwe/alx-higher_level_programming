#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    try:
        while j is not x:
            print(my_list[j], end='')
            j = j + 1
    except IndexError:
        None
    print()
    return j