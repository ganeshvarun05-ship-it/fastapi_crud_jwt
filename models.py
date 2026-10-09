from datetime import datetime, timedelta
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True,  nullable=False)
    password = Column(String, nullable=False)

class product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True,nullable=False)
    description = Column(String, unique=True, nullable=False)
    owner_id = Column(Integer)

class price(Base):
    __tablename__ = "prices"
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False) 