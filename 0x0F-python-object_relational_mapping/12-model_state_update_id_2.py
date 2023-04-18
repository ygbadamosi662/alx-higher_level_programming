#!/usr/bin/python3
"""
Adds a state instance to hbtn_0e_6_usa
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

    new_state = State(name='Louisiana')
    update = session.query(State).filter(State.id == 2).first()

    update.name = 'New Mexico'
    session.commit()
