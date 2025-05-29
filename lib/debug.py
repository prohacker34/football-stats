from helpers import get_all_players

def debug_view():
    players = get_all_players()
    print("📋 Players:")
    for player in players:
        team_name = player.team.name if player.team else "No Team"
        skills = ", ".join([skill.name for skill in player.skills]) if player.skills else "No Skills"
        print(f" - {player.name}: Goals: {player.goal}, Team: {team_name}, Skills: {skills}")

if __name__ == '__main__':
    debug_view()
