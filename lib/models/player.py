from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.init import Base

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, autoincrement=True)  
    name = Column(String, nullable=False)
    goal = Column(Integer, default=0)
    team_id = Column(Integer, ForeignKey('teams.id'))

    team = relationship("Team", back_populates="players")


class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)

    players = relationship("Player", back_populates="team")
