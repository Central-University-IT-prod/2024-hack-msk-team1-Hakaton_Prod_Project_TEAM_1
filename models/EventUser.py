from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DBSession = scoped_session(sessionmaker())
class _Base(object):
    query = DBSession.query_property()

Base = declarative_base(cls=_Base)

class EventUser(Base):
    __tablename__ = 'event_user'  # Имя таблицы в базе данных

    event_id = Column(Integer)
    user_id = Column(Integer)
