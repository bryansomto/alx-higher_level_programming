#!/usr/bin/python3
# List state database hbtn_0e_0_usa
# Syntax: ./0-select_states.py username password database_name
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    [print(state) for state in cur.fetchall()]
