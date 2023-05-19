from .utils import IDName

__all__ = ['Item']


class Item:

    def __init__(self, data: dict) -> None:
        self.id = data['id']
        self.name = data['name']
        self.description = d if (d := data['description']) else "Not provided."

        self.sellPrice = data['sellPrice'] / 10
        self.buyPrice = data['buyPrice'] / 10

        self.craftable = True if data['craftable'] == 1 else False

        self.rarity = IDName(data['rarityId'], data['rarityName'])
        self.category = IDName(data['categoryId'], data['categoryName'])
        self.type = IDName(data['typeId'], data['typeName'])
        self.faction = IDName(data['factionId'], data['factionName'])

        self.imagePath = data['imagePath']