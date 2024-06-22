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
        query = f"SELECT * FROM states WHERE name LIKE BINARY '{search}' ORDER BY id ASC"
        cur.execute(query)
        results = cur.fetchall()

        for row in results:
            print(row)

    except MySQLdb.Error:
        try:
            print("MySQLdb Error")
        except IndexError:
            print("MySQLdb Error - IndexError")

    cur.close()
    conn.close()
