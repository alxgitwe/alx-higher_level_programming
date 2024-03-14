#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    a = len(sys.argv) - 1
    b = 0

    for i in range(a):
        b = b + int(sys.argv[i + 1])
    print("{:d}".format(b))
