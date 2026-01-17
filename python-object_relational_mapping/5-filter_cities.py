#!/usr/bin/python3
"""
This script lists all cities of a given state from a MySQL database,
safe from SQL injection.
"""

import MySQLdb
import sys


def main():
    """Connects to MySQL and lists all cities of a given state."""
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC;"
    )

    cursor.execute(query, (state_name,))
    cities = cursor.fetchall()

    print(", ".join(city[0] for city in cities))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
