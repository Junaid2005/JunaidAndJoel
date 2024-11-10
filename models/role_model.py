# models/role_model.py
from sqlalchemy import Column, Integer, String
from . import Base



class Role(Base):
    __tablename__ = 'roles'

    roleId = Column(Integer, primary_key=True)
    roleName = Column(String, unique=True)
