#!/usr/bin/python3
"""sends a request to the URL"""
import requests
import sys

if __name__ == "__main__":
    u = sys.argv[1]
    res = requests.get(u)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
