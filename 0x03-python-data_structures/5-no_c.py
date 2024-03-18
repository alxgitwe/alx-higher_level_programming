#!/usr/bin/python3
def no_c(my_string):
    string_t = ""
    for a in range(len(my_string)):
        if my_string[a] != 'c' and my_string[a] != 'C':
            string_t = string_t + my_string[a]
    return string_t
