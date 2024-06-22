#!/usr/bin/python3
"""
    script
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )
    cur = conn.cursor()

    try:
        search = argv[4]
        query = f"SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cur.execute(query, (search,))
        results = cur.fetchall()
    except MySQLdb.Error:
        try:
            results = ("MySQLdb Error")
        except IndexError:
            results = ("MySQLdb Error - IndexError")

    for row in results:
        print(row)

    cur.close()
    conn.close()
