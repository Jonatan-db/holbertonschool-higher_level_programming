#!/usr/bin/python3


def getAllCities(user2, passward2, db2):
    """ script that gets all the states when called on """
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_city import Base, City
    from relationship_state import State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                user2, passward2, db2))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    c1 = City(name="San Francisco")
    s1 = State(name="California", cities = [c1])

    session.add(s1)
    session.add(c1)

    session.commit()
    session.close()
    # engine = sqlalchemy.create_engine()
    # db = MySQLdb.connect(host=MY_HOST, user=MY_USER, db=MY_DB)
    # cur = db.cursor()

if __name__ == "__main__":
    import sys
    """ protected from executing when imported """
    getAllCities(sys.argv[1], sys.argv[2], sys.argv[3])
