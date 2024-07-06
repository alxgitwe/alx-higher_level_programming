#!/usr/bin/python3
"""multiple technical challenges"""
if __name__ == '__main__':
    from sys import argv
    import requests
    res = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    c = res.json()
    for co in c[:10]:
        print(co.get('sha'), end=': ')
        print(co.get('commit').get('author').get('name'))
