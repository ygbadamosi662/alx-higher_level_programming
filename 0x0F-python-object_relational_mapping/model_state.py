#!/usr/bin/python3
"""
Defines a class State an intance of Base = declarative_base()
"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

if __name__ == "__main__":
    Base = declarative_base()

    class State(Base):
        __tablename__ = 'states'

        id = Column(Integer, primary_key=True, nullable=False,
                    autoincrement=True)
        name = Column(String(128), nullable=False)

    url = 'mysql+mysqldb://root:password@localhost:3306/hbtn_0e_6_usa'
    engine = create_engine(url)

    Base.metadata.create_all(engine)
