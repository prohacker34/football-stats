from helpers import create_database, add_player

def main():
    create_database()

    while True:
        entry = input("player name, goal (leave blank to quit): ")
        if not entry:
            break
        if ',' not in entry:
            print("⚠️ Format: Name, Goal")
            continue

        name, goal = [p for p in entry.split(',', 1)]
        add_player(name, goal)
        print(f"✅ Added {name} with goal {goal}")

if __name__ == '__main__':
    main()
