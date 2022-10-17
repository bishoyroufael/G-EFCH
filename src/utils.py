from schemas.city import City
from schemas.state import State
import json
from difflib import SequenceMatcher

class Utils():
    def __init__():
        pass


    @staticmethod
    def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()

    @staticmethod
    def add_states_countires_db(db):

        present = db.session.execute(db.select(State)).all()
        if present:
            return

        with open('src/assets/germany_long.json', encoding='utf8') as jd:
            germany_data = json.load(jd)
            states_data = sorted(set([item["state"] for item in germany_data]))
            map = {}
            for state in states_data:
                map[state] = []

            for item in germany_data:
                map [item["state"]].append((item["name"], item["coords"]["lat"], item["coords"]["lon"]))

            for state in states_data:
                state_db = State(state)
                cities_db = [City(c_d[0], c_d[1], c_d[2]) for c_d in map[state]]
                state_db.cities = cities_db
                db.session.add(state_db)
                db.session.commit()
