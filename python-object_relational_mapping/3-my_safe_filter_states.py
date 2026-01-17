#!/usr/bin/python3
"""
This script safely displays all states whose name matches the given argument
from a MySQL database, protecting against SQL injection.
"""

import MySQLdb
import sys


def main():
    """Connects to a MySQL database and safely filters states by user input."""
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
        "SELECT * FROM states "
        "WHERE BINARY name = %s "
        "ORDER BY id ASC;"
    )

    cursor.execute(query, (state_name,))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
