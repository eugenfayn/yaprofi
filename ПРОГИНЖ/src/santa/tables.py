import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from typing import List

Base = declarative_base()

class Group(Base):
    __tablename__='groups'

    id = sa.Column(sa.Integer,primary_key='True')
    name = sa.Column(sa.String)
    description = sa.Column(sa.String,nullable=True)
    participants = relationship('Participant',back_populates='group_name')

class Participant(Base):
    __tablename__='participants'
    id =  sa.Column(sa.Integer,primary_key='True')
    name =  sa.Column(sa.String)
    group_id = sa.Column(sa.Integer,sa.ForeignKey('groups.id'))
    group_name = relationship('Group',back_populates='participants')
    wish = sa.Column(sa.String,nullable=True)
    recipient = sa.Column(sa.String,sa.ForeignKey('participants.id'),nullable=True)
    

#from santa.tables import Base
#from santa.db import engine
#Base.metadata.create_all(engine)