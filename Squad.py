from math import floor

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
        sum_rating = 0
        for player in self.players:
            sum_rating = sum_rating + player.rating

        average_rating = sum_rating / len(self.players)

        for player in self.players:
            if player.rating > average_rating:
                if self.players.index(player) < 11:
                    sum_rating += player.rating - average_rating
                else:
                    sum_rating += .5 * (player.rating - average_rating)

        rounded = round(sum_rating)

        rating = min(max(floor(rounded / len(self.players)), 0), 99)

        return rating

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

