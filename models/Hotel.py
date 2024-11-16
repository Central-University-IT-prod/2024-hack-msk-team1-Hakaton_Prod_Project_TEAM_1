from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DBSession = scoped_session(sessionmaker())
class _Base(object):
    query = DBSession.query_property()

Base = declarative_base(cls=_Base)

class Hotel(Base):
    __tablename__ = 'hotel'  # Имя таблицы в базе данных

    id = Column(Integer, primary_key=True)
    price = Column(Integer)
    name = Column(String)
