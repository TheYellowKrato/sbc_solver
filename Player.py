class Player:

    def __init__(self):
        self.bricked = False
        self.position = "default"
        self.id = -1
        self.resource_id = -1
        self.rating = 0
        self.chem = 0
        self.rare = False
        self.club_id = -1
        self.league_id = -1
        self.nationality_id = -1

    def __repr__(self):
        return str(self.__dict__)
