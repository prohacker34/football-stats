
from helpers import create_database, seed_players

if __name__ == '__main__':
    create_database()
    seed_players()
    print("✅ Database seeded.")

