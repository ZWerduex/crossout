from .CrossoutDBAPI import CrossoutDBAPI
from .objects import *


__all__ = ['CrossoutDB']


class CrossoutDB:

    def __init__(self):
        super().__init__()
        self.api = CrossoutDBAPI()

    def items(self,
            rarity: str | None = None,
            category: str | None = None,
            faction: str | None = None,
            query: str | None = None
        ) -> list[Item]:
        return [Item(item) for item in self.api.items(
            rarity=rarity,
            category=category,
            faction=faction,
            query=query
        )]
    
    def item(self, item_id: int) -> Item:
        return Item(self.api.item(item_id))

    def factions(self) -> list[Entity]:
        return [Entity(f['id'], f['name']) for f in self.api.factions()]
    
    def recipe(self, item: Item) -> Recipe:
        r = self.api.recipe(item.id)
        assert r['item']['id'] == item.id

        items = []
        ressources = []
        price = 0
        
        for ing in r['ingredients']:
            if ing['item']['categoryName'] == 'Resources':
                ressources.append(
                    (Resource(self.api.item(ing['item']['id'])), ing['number'])
                )
            elif ing['item']['name'].endswith('Bench Cost'):
                price += ing['item']['buyPrice'] / 100
            else:
                items.append(
                    (self.item(ing['item']['id']), ing['number'])
                )

        return Recipe(items, ressources, price)
