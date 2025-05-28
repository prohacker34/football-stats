
from models.init import Base, Session, engine
from models.player import Player


def create_database():
    Base.metadata.create_all(engine)

def add_player(name, goal):
    session = Session()
    player = Player(name=name, goal=goal)
    session.add(player)
    session.commit()
    session.close()

def get_all_players():
    session = Session()
    players = session.query(Player).all()
    session.close()
    return players

def seed_players():
    session = Session()
    players= [
        Player(name="Alex", goal=3),
        Player(name="Bob", goal=2),
        Player(name="Charlie", goal=1)
    ]
    session.add_all(players)
    session.commit()
    session.close()
