#!/usr/bin/python3
"""sends a request to the URL"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    r = urllib.request.Request(sys.argv[1])
    try:
        urllib.request.urlopen(r)
        with urllib.request.urlopen(r) as res:
            b = res.read().decode('utf-8')
            print(b)
    except urllib.error.HTTPError as k:
        print("Error code: {}".format(k.code))
