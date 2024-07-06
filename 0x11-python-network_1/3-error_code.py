#!/usr/bin/python3
import urllib.request
import urllib.error
import sys

if len(sys.argv) != 2:
    print("Usage: ./3-error_code.py <URL>", file=sys.stderr)
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))

