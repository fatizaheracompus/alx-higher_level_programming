#!/usr/bin/python3
""" script lists all states from database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    dbe = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], dbe=sys.argv[3], port=3306)
    cure = dbe.cursor()
    cure.execute("SELECT * FROM states")
    rows = cure.fetchall()
    for row in rows:
        print(row)
    cure.close()
    dbe.close()
