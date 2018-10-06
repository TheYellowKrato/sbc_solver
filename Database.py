import pymongo


class Database:
    con = None
    table = None

    def __init__(self):
        self.con = pymongo.MongoClient("mongodb://localhost:27017/")
        self.table = self.con["fut19"]

    def load_challenge(self, challenge_id):
        return self.table["challenges"].find_one({"challengeId": challenge_id})

