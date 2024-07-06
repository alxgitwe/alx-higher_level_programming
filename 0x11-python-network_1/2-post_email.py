#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    u = sys.argv[1]
    v = {"email": sys.argv[2]}
    d = urllib.parse.urlencode(v).encode("ascii")

    r = urllib.request.Request(u, d)
    with urllib.request.urlopen(r) as r:
        print(r.read().decode("utf-8"))

