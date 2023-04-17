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
    stateName = sys.argv[4]

    mydb = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=dbName)
    cursor = mydb.cursor()
    quer = "SELECT cities.name FROM cities JOIN states ON states.id = "
    quer = quer + "cities.state_id WHERE states.name = %s"
    cursor.execute(quer, (stateName,))
    cities = cursor.fetchall()
    str = ""
    inx = 0
    deli = ", "

    for city in cities:
        if inx == len(cities) - 1:
            str = str + city[0]
            break
        str = str + city[0] + deli
        inx = inx + 1
    print(str)
    cursor.close()
    mydb.close()
