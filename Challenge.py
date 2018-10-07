from Squad import Squad


class Challenge:
    squad = None
    data = None

    def __init__(self, challenge_data):
        self.data = challenge_data
        self.squad = Squad(challenge_data["formation"], challenge_data["playerRequirements"])



