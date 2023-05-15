import json


import crossoutapi


if __name__ == "__main__":
    api = crossoutapi.CrossoutDBAPI()
    with open("item.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(api.item(7), indent=4))