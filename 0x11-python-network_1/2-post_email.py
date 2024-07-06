#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed"""
import urllib.request
import urllib.parse
import sys

if len(sys.argv) != 3:
    print("Usage: ./2-post_email.py <URL> <email>", file=sys.stderr)
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('ascii')

with urllib.request.urlopen(url, data) as response:
    print(response.read().decode('utf-8'))

