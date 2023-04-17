#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_0_usa
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
    quer = "SELECT cities.id, cities.name, states.name  FROM cities JOIN "
    quer = quer + "states ON cities.state_id = states.id ORDER BY id ASC"
    cursor.execute(quer)
    cities = cursor.fetchall()

    for city in cities:
        print(city)
    cursor.close()
    mydb.close()
