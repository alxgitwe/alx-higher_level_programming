#!/usr/bin/python3
"""
script
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor object
    cur = db.cursor()

    # Execute
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch
    for row in cur.fetchall():
        print(row)

    # Close database connection
    cur.close()
    db.close()
