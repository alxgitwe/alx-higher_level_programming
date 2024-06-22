#!/usr/bin/python3
"""
    script
"""
from sys import argv
from model_city import Base, City
from model_state import Base as State_Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = session.query(State).filter_by(id=city.state_id).first().name
        print(f"{state_name}: ({city.id}) {city.name}")

    session.close()
