#!/usr/bin/python3
"""  """
import requests
import sys


if __name__ == "__main__":
    e = {'email': sys.argv[2]}
    res = requests.post(sys.argv[1], data=e)
    print(res.text)
