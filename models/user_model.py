
from sqlalchemy import Column, Integer, Boolean
from . import Base

# User Model
class User(Base):
    __tablename__ = 'users'

    userId = Column(Integer, primary_key=True)
    admin = Column(Boolean, default=False)
    wins = Column(Integer, default=0)



