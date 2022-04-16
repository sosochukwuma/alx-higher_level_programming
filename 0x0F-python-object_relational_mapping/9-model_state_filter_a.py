#!/usr/bin/python3
''' Write a script that lists all State objects
that contains the letter a from the database '''

from sys import argv
from requests import Session
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State.id, State.name).from_statement(text(
        "SELECT id, name "
        "FROM states "
        "WHERE name REGEXP '^.*a.*' "
    )).all()
    for id, name in rows:
        print("{:d}: {:s}".format(id, name))
    session.close()