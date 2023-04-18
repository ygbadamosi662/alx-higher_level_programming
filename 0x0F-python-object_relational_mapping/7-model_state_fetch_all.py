#!/usr/bin/python3
"""
Gets all states from hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    url = url.format(sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(url)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)

    for state in states:
        print("{}: {}".format(state.id, state.name))
