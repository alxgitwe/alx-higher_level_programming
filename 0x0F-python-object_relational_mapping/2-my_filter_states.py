#!/usr/bin/python3
""" Filter States """
import MySQLdb
from sys import argv

def filter_states():
    """ Filter states by name """
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = db.cursor()
    sql_string = "SELECT * FROM states WHERE name LIKE BINARY %s"
    cur.execute(sql_string, (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    filter_states()
