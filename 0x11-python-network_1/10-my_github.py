#!/usr/bin/python3
"""GitHub"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    k = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", auth=k)
    print(res.json().get("id"))
