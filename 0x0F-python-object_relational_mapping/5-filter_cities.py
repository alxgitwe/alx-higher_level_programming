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
        state_name = argv[4]
        query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """
        cur.execute(query, (state_name,))
        results = cur.fetchall()

        if results:
            print(", ".join(city[0] for city in results))
        else:
            print()
    except MySQLdb.Error:
        try:
            print("MySQLdb Error")
        except IndexError:
            print("MySQLdb Error - IndexError")

    cur.close()
    conn.close()
