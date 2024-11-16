from mox.Hotel import Hotel as h
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from models.Hotel import Hotel


engine = create_engine('sqlite:///hakaton.db')

for i in range(20):
    Session = sessionmaker(bind=engine)
    session = Session()

    hotel = h()
    hotel = hotel.fill()

    room = Hotel(name=hotel.name, price=hotel.price)

    session.add(room)  # Добавляем его в сессию
    session.commit()

    Session = sessionmaker(bind=engine)
    session_db = Session()

    accounts = session_db.execute(select(Hotel)).scalars().all()
    print(accounts)