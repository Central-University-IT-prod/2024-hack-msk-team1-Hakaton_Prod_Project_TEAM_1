from sqlalchemy import Column, Integer, String, TIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DBSession = scoped_session(sessionmaker())
class _Base(object):
    query = DBSession.query_property()

Base = declarative_base(cls=_Base)


class Event(Base):
    __tablename__ = 'event'  # Имя таблицы в базе данных

    id = Column(Integer, primary_key=True)  # Столбец id, первичный ключ
    spending = Column(Integer)  # Столбец username, не может быть null
    reason = Column(String)
    date = Column(TIME, nullable=False)
