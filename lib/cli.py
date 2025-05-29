from helpers import create_database, add_player, add_team

def main():
    create_database()

    while True:
        print("\nOptions:")
        print("1. Add Player")
        print("2. Add Team")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            entry = input("player name, goal (leave blank to quit): ")
            if not entry.strip():
                continue
            if ',' not in entry:
                print("⚠️ Format: Name, Goal")
                continue

            try:
                name, goal = [p.strip() for p in entry.split(',', 1)]
                if not name or not goal.isdigit():
                    print("⚠️ Invalid input. Ensure the name is not empty and the goal is a number.")
                    continue

                add_player(name, int(goal))
                print(f"✅ Added {name} with goal {goal}")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "2":
            team_name = input("Enter team name: ").strip()
            if not team_name:
                print("⚠️ Team name cannot be empty.")
                continue

            try:
                add_team(team_name)
                print(f"✅ Team '{team_name}' added.")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please select 1, 2, or 3.")

if __name__ == '__main__':
    main()
