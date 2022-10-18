import json


class readJson:
    def __init__(self):
        pass

    # It will get json value in json file (./setup/vars.json)
    def getJson(self, jsonFile):
        with open(jsonFile, "r") as f:
            value = json.load(f)
        return value
