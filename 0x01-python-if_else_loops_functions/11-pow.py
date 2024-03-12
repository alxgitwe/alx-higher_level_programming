#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b < 0:
        b = -b
        pow = a
        while b > 1:
            pow = pow * a
            b = b - 1
        return 1 / pow
    else:
        pow = a
        while b > 1:
            pow = pow * a
            b = b - 1
        return pow
