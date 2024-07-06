#!/usr/bin/python3
"""sends a request to the URL and displays the value"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        k = response.getheader('X-Request-Id')
        print(k)
