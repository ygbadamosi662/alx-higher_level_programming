#!/usr/bin/python3
"""
Defines a class State an intance of Base = declarative_base()
"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
import sys
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    Base = declarative_base()

    class State(Base):
        __tablename__ = 'states'

        id = Column(Integer, primary_key=True, nullable=False,
                    autoincrement=True)
        name = Column(String(128), nullable=False)

    url = 'mysql://{}:{}@localhost/{}'
    url = url.format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)

    Base.metadata.create_all(engine)
