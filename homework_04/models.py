"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""


import os

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

engine = create_async_engine(PG_CONN_URI, echo=True)
Base = declarative_base(bind=engine)
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class User(Base):
    """ Модель Пользователь. """
    __tablename__ = 'users'

    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(128), nullable=False, default='', server_default='')
    username = Column(String(32), nullable=False, default='', server_default='')
    email = Column(String(128), nullable=False, default='', server_default='')
    posts = relationship('Post', back_populates='user')


class Post(Base):
    """ Модель Публикации. """
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(128), nullable=False, default='', server_default='')
    body = Column(String(256), nullable=False, default='', server_default='')
    user = relationship('User', back_populates='posts')
