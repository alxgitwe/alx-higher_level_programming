#!/usr/bin/python3
"""request to the passed URL"""
import requests
import sys


if __name__ == "__main__":
    u = sys.argv[1]
    v = {"email": sys.argv[2]}

    res = requests.post(u, data=v)
    print(res.text)
