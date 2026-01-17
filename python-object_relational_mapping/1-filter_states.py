#!/usr/bin/python3
"""
This script lists all states starting with the letter N
from a MySQL database.
"""

import MySQLdb
import sys


def main():
    """Connects to a MySQL database and prints states starting with 'N'."""
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states "
        "WHERE name LIKE BINARY 'N%' "
        "ORDER BY id ASC;"
    )

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
