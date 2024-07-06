#!/usr/bin/python3
"""GitHub"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    q = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", aut=q)
    print(res.json().get("id"))
