from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, String, MetaData, Text)

from flask_login import UserMixin

metadata = MetaData()
Base = declarative_base(metadata=metadata)

class User(UserMixin, Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    username = Column(String(100), unique=True)
    password = Column(String(100))
    meta_data = Column(Text)