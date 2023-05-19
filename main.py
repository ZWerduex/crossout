import json


import crossout


if __name__ == "__main__":
    api = crossout.CrossoutDB()
    print(api.factions())
    