#!/usr/bin/python3
"""sends a request to the URL and displays the value of the variable"""
import requests
import sys

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    k = res.headers.get('X-Request-Id')
    print(k)
