#!/usr/bin/python3
def remove_char_at(str, n):
    strr = ""
    for a, b in enumerate(str):
        if a != n:
            strr += b

    return strr
