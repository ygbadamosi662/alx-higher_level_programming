#!/usr/bin/python3
"""
Defines a class State an intance of Base = declarative_base
"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

Base = declarative_base()


class State(Base):

    """
    Defines a class State
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    url = 'mysql+mysqldb://root:password@localhost:3306/database'

    engine = create_engine(url)

    Base.metadata.create_all(engine)
