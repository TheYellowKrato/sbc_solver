from Player import Player


class Squad:

    def __init__(self):
        self.players = []
        self.formation = "default"
        for i in range(0, 11):
            player = Player()
            self.players.append(player)

    def __repr__(self):
        return str(self.__dict__)

    def get_global_rating(self):
        global_rating = 0
        for player in self.players:
            global_rating = global_rating + player.rating
            global_rating = global_rating / len(self.players)
        return global_rating

    def get_global_chemistry(self):
        pass

    def count_rare(self):
        rare_count = 0
        for player in self.players:
            if player.rare:
                rare_count = rare_count + 1
        return rare_count

    def get_nationality(self):
        nationality = {}
        for player in self.players:
            if player.nationality_id in nationality:
                nationality[player.nationality_id] = nationality[player.nationality_id] + 1
            else:
                nationality[player.nationality_id] = 1
        return nationality

    def get_leagues(self):
        leagues = {}
        for player in self.players:
            if player.league_id in leagues:
                leagues[player.league_id] = leagues[player.league_id] + 1
            else:
                leagues[player.league_id] = 1
        return leagues

    def get_clubs(self):
        clubs = {}
        for player in self.players:
            if player.club_id in clubs:
                clubs[player.club_id] = clubs[player.club_id] + 1
            else:
                clubs[player.club_id] = 1
        return clubs

