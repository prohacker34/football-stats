from models.init import Base, Session, engine
from models.player import Player, Team


def create_database():
    
    Base.metadata.create_all(engine)


    session = Session()


    if not session.query(Team).first():

        team_a = Team(name="Team A")
        team_b = Team(name="Team B")
        session.add_all([team_a, team_b])


        player1 = Player(name="Alex", goal=3, team=team_a)
        player2 = Player(name="Bob", goal=2, team=team_a)
        player3 = Player(name="Charlie", goal=1, team=team_b)
        session.add_all([player1, player2, player3])

        session.commit()
        print("✅ Default data seeded.")
    else:
        print("ℹ️ Database already seeded.")

    session.close()


def add_player(name, goal, team_name=None):
    session = Session()
    team = session.query(Team).filter_by(name=team_name).first() if team_name else None
    player = Player(name=name, goal=goal, team=team)
    session.add(player)
    session.commit()
    session.close()


def get_all_players():
    session = Session()
    players = session.query(Player).all()
    session.close()
    return players


def add_team(name):
    session = Session()
    team = Team(name=name)
    session.add(team)
    session.commit()
    session.close()
