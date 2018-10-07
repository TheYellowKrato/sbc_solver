from math import floor

from FormationsParser import FormationsParser
from Player import Player
from Slot import Slot


class Squad:

    def __init__(self, formation, player_requirements):
        self.slots = []
        formation_parser = FormationsParser()
        self.formation = formation
        players_formations = formation_parser.identify_formation(self.formation)
        player_requirements.reverse()

        for i in range(0, 11):
            slot = Slot()
            slot.position = players_formations.pop()
            player_requirement = player_requirements.pop()
            if player_requirement["playerType"] == "BRICK":
                slot.is_bricked = True
            elif player_requirement["playerType"] == "CUSTOM_BRICK":
                slot.is_bricked = True
                player = Player()
                for req in player_requirement["elgReq"]:
                    if req["type"] == "NATION_ID":
                        player.nationality_id = req["eligibilityValue"]
                    if req["type"] == "LEAGUE_ID":
                        player.league_id = req["eligibilityValue"]
                    if req["type"] == "CLUB_ID":
                        player.club_id = req["eligibilityValue"]
                slot.player = player
            self.slots.append(slot)

    def __repr__(self):
        return str(self.__dict__)

    def get_global_rating(self):
        sum_rating = 0
        for slot in self.slots:
            sum_rating = sum_rating + slot.player.rating

        average_rating = sum_rating / len(self.slots)

        for slot in self.slots:
            if slot.player.rating > average_rating:
                if self.slots.index(slot) < 11:
                    sum_rating += slot.player.rating - average_rating
                else:
                    sum_rating += .5 * (slot.player.rating - average_rating)

        rounded = round(sum_rating)

        rating = min(max(floor(rounded / len(self.slots)), 0), 99)

        return rating

    def get_global_chemistry(self):
        pass

    def count_rare(self):
        rare_count = 0
        for slot in self.slots:
            if slot.player.is_rare:
                rare_count = rare_count + 1
        return rare_count

    def get_nationalities(self):
        nationality = {}
        for slot in self.slots:
            if slot.player.nationality_id in nationality:
                nationality[slot.player.nationality_id] = nationality[slot.player.nationality_id] + 1
            else:
                nationality[slot.player.nationality_id] = 1
        return nationality

    def get_leagues(self):
        leagues = {}
        for slot in self.slots:
            if slot.player.league_id in leagues:
                leagues[slot.player.league_id] = leagues[slot.player.league_id] + 1
            else:
                leagues[slot.player.league_id] = 1
        return leagues

    def get_clubs(self):
        clubs = {}
        for slot in self.slots:
            if slot.player.club_id in clubs:
                clubs[slot.player.club_id] = clubs[slot.player.club_id] + 1
            else:
                clubs[slot.player.club_id] = 1
        return clubs

