import json
from pprint import pprint


def GetHeroFromID(hID):
    with open("my_heroes.json") as heroList:
        data = json.load(heroList)
        return data[str(hID)]
