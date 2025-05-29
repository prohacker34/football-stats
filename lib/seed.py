from helpers import create_database, add_team, add_player

if __name__ == '__main__':
    create_database()

    
    add_team("Team A")
    add_team("Team B")


    add_player(name="Alex", goal=3, team_name="Team A")
    add_player(name="Bob", goal=2, team_name="Team A")
    add_player(name="Charlie", goal=1, team_name="Team B")

    print("✅ Database seeded.")

