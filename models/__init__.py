import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = os.path.abspath('users.db')
engine = create_engine(f'sqlite:///{DATABASE_URL}', echo=True)

Session = sessionmaker(bind= engine)

Base = declarative_base()