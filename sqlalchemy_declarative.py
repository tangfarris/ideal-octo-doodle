import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
class Posts(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)    
    image = Column(String(50), nullable=False)
    content = Column(String(250), nullable=False)
    