#!/usr/bin/python3
"""
Gets State instance that matches the 4th argument passed to this script from\
        states in hbtn_0e_6_usa
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

    state = session.query(State).filter(State.name == sys.argv[4]).first()

    if state:
        print(state.id)
    else:
        print("Not found")
