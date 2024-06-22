#!/usr/bin/python3
"""
script
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create object
    cur = db.cursor()

    # Execute
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (sys.argv[4],))

    # Fetch
    for row in cur.fetchall():
        print(row)

    # Close
    cur.close()
    db.close()
