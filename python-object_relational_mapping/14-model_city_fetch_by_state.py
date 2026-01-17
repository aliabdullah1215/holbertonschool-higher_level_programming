#!/usr/bin/python3
"""
This script lists all City objects from the database
along with their corresponding State names using SQLAlchemy ORM.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    """Connects to the database and prints cities by state."""
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            user, password, database
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    results = (
        session.query(City, State)
        .filter(City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()


if __name__ == "__main__":
    main()
