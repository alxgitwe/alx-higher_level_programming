#!/usr/bin/python3
"""script that takes in a letter"""
import requests
import sys

if __name__ == "__main__":
    l = "" if len(sys.argv) == 1 else sys.argv[1]
    p = {"q": l}

    res = requests.post("http://0.0.0.0:5000/search_user", data=p)
    try:
        resp = res.json()
        if resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp.get("id"), resp.get("name")))
    except ValueError:
        print("Not a valid JSON")
