#!/usr/bin/python3
"""fetches url"""
import requests

response = requests.get('https://alx-intranet.hbtn.io/status')
body = response.text

print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))

