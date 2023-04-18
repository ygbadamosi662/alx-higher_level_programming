#!/usr/bin/python3
"""
Gets first State instance from states in hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    url = url.format(sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(url, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
