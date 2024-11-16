from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import *
import dotenv
import os
from flask import Flask, session, redirect, request, render_template, abort



DBSession = scoped_session(sessionmaker())
class _Base(object):
    query = DBSession.query_property()

Base = declarative_base(cls=_Base)

class User(Base):
    __tablename__ = 'user'  # Имя таблицы в базе данных

    id = Column(Integer, primary_key=True)  # Столбец id, первичный ключ
    username = Column(String, nullable=False)     # Столбец username, не может быть null
    password = Column(String,  nullable=False) # password not null
    login = Column(String, nullable=False)
