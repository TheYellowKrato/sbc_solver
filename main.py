from Database import Database
from FormationsParser import FormationsParser
from Squad import Squad

if __name__ == "__main__":

    database = Database()
    formation_parser = FormationsParser()

    challenge = database.load_challenge(27)

    player_requirements = challenge["playerRequirements"]
    current_formation = challenge["formation"]

    players_formations = formation_parser.identify_formation(current_formation)
    players_formations.reverse()

    squad = Squad()
    squad.formation = current_formation

    #TODO : Load bricked nationality and stuff ... ex Lucas Moura PTM
    for player in player_requirements:
        index = player["index"]
        squad.players[index].id = index
        squad.players[index].position = players_formations.pop()
        if player["playerType"] == "BRICK":
            squad.players[index].bricked = True

    print(squad)
