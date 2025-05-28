from helpers import get_all_players

def debug_view():
    players = get_all_players()
    print("📋 players:")
    for player in players:
        print(f" - {player.name}: {player.goal}")

if __name__ == '__main__':
    debug_view()
