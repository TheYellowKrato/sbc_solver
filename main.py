from Challenge import Challenge
from Database import Database
from FormationsParser import FormationsParser

if __name__ == "__main__":

    database = Database()
    formation_parser = FormationsParser()

    challenge_data = database.load_challenge(39)

    challenge = Challenge(challenge_data)
