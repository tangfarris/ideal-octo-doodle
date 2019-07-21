import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
class Images(Base):
    __tablename__ = 'image'
    id = Column(Integer, primary_key=True)
    image = Column(String(50), nullable=False)
    credit = Column(String(50), nullable=False)
    content = relationship('Content', backref='image', lazy=True)

    def __init__(self, id, image, credit):
        self.id = id
        self.image = image
        self.credit = credit        

# attempt to establish one to many relationship
# expressed with relationship() function, but foreign key
# has to be seperately declared with ForeignKey class.
# ** relationship() returns a new property that can do multiple things. point at
# other class and load multiple of them. how does it know it will return more than
# one 'content'?
# backref is a simple way to declare a new property of content class.
# lazy defines when sqlalchemy will load the data from database.
#
class Content(Base):
    __tablename__ = 'content'
    id = Column(Integer, primary_key=True)
    name = Column(String(88), nullable=False)
    link = Column(String(150), nullable=False)
    description = Column(String(150), nullable=False)    
    image_id = Column(Integer, ForeignKey('image.id'), nullable=False)

    def __init__(self, id, name, link, description, image_id):
        self.id = id
        self.name = name
        self.link = link
        self.description = description        
        self.image_id = image_id

engine = create_engine('sqlite:///my.db')
Base.metadata.create_all(engine)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base.query = db_session.query_property()                                         
# interacting with db
# from app import Images
# from app import db
# new_obj = Images(newid, 'image link', 'links')
# db.session.add(new_obj)
# db.session.commit()

# for updating a row, need Base.query = db_session.query_property().
# db.session.query(User).filter(User.id==7).delete()
# db.session.query(Content).filter(Content.id==11).update
# . . . ({'name':'Twelve South Bookarc for Macbook (Amazon): '})

# image id: 5
# content id: 30

# from app import Images
# from app import Content
# from app import db
