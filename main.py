import json

import crossout

def toJson(obj):
    with open('thing.json', 'w', encoding='utf-8') as out:
        json.dump(obj, out, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    api = crossout.CrossoutDB()
    r = api.recipe(api.item(456))