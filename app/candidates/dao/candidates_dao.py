import json


class CandidateDAO:
    def __init__(self, path: str):
        """ Creating a DAO instance,  it is needed to specify the path to the JSON file """
        self.path = path

    def load_data(self) -> list:
        """ Loads data from file and return a list"""
        with open(self.path, encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_all(self):
        """ Returns a list with all data """
        candidates = self.load_data()
        return candidates

    def get_by_pk(self, pk):
        """ Returns one candidate by his pk """
        candidates = self.load_data()
        for candidate in candidates:
            if candidate["pk"] == pk:
                return candidate
