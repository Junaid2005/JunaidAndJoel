import os.path
import sys

from sqlalchemy import create_engine, Column, Integer, Boolean
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.testing.suite.test_reflection import users

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.logger import logger

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'  # Table name

    userId = Column(Integer, primary_key=True)
    admin = Column(Boolean, default=False)
    wins = Column(Integer, default=0)

db_path = os.path.abspath('users.db')
engine = create_engine(f'sqlite:///{db_path}', echo=True)


Base.metadata.create_all(bind= engine)

Session = sessionmaker(bind= engine)
session = Session()

def add_user(user_id):
    if not get_user(user_id):
        try:
            new_user = User(userId=user_id)
            session.add(new_user)
            session.commit()
            logger.info(f"User {user_id} added!")
        except SQLAlchemyError as e:
            logger.error(f"Failed to create user with {user_id}: Database error {e}")

    else:
        logger.error(f"User with {user_id} already exists")

def get_user(user_id):
    user = session.query(User).filter(User.userId == user_id).first()
    if user:
        return user
    else:
        return None

def increment_wins(user_id):
    user = session.query(User).filter(User.userId == user_id)


def get_users():
    user_list = session.query(User).all()
    for user in user_list:
        print(f"User ID: {user.userId}, Admin: {user.admin}, Wins: {user.wins}")

add_user(1)
add_user(2)
get_users()
increment_wins(1)


