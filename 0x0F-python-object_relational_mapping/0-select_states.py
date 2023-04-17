#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]

    mydb = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=dbName)
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)
