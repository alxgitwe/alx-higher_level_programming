#!/usr/bin/python3
"""sends a request to the URL and displays the value"""
import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: ./1-hbtn_header.py <URL>", file=sys.stderr)
    sys.exit(1)

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    print(response.info().get('X-Request-Id'))

