class Slot:

    player = None
    is_bricked = False
    position = None
    link = None
    chemistry = 0

    def __init__(self):
        self.player = None

    def load_player(self, player):
        pass

    def __repr__(self):
        return str(self.__dict__)
