class Player:

    def __init__(self):
        self.resource_id = -1
        self.rating = 0
        self.preferred_position = "default"
        self.club_id = -1
        self.nationality_id = -1
        self.league_id = -1
        self.loyalty = False
        self.is_rare = False

    def __repr__(self):
        return str(self.__dict__)





