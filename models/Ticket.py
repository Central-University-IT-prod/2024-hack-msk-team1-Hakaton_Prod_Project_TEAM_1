from sqlalchemy import TIME, Column, Integer, String, TIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DBSession = scoped_session(sessionmaker())
class _Base(object):
    query = DBSession.query_property()

Base = declarative_base(cls=_Base)


class Ticket(Base):
    __tablename__ = 'ticket'  # Имя таблицы в базе данных

    id = Column(Integer, primary_key=True)  # Столбец id, первичный ключ
    price = Column(Integer)  # Столбец username, не может быть null
    race_number = Column(String)
    date_arrive = Column(TIME, nullable=False)
    date_comeback = Column(TIME, nullable=False)
    home = Column(String)
    away = Column(String)

