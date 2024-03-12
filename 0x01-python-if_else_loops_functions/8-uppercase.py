#!/usr/bin/python3
def islower(c):
    a = ord(c)
    if a >= 97 and a <= 122:
        return True
    else:
        return False


def uppercase(str):
    for a in str:
        print("{:c}".format(ord(a) - 32 if islower(a) else ord(a)), end="")
    print("")
