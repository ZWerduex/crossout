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
    
    def _buildEntitySet(self, objects: set[dict]) -> set[Entity]:
        return {Entity(o['id'], o['name']) for o in objects}

    def rarities(self) -> set[Entity]:
        return self._buildEntitySet(self.api.rarities())
    
    def categories(self) -> set[Entity]:
        return self._buildEntitySet(self.api.categories())

    def factions(self) -> set[Entity]:
        return self._buildEntitySet(self.api.factions())
    
    def types(self) -> set[Entity]:
        return self._buildEntitySet(self.api.types())
    
    def recipe(self, item: Item) -> Recipe:
        r = self.api.recipe(item.id)
        assert r['item']['id'] == item.id

        items = []
        resources = []
        workbench = Workbenches.fromName(item.rarity.name)
        
        for ing in r['ingredients']:
            if ing['item']['categoryName'] == 'Resources':
                resources.append(
                    (Resource(self.api.item(ing['item']['id'])), ing['number'])
                )
            else:
                items.append(
                    (self.item(ing['item']['id']), ing['number'])
                )

        return Recipe(items, resources, workbench, item.faction)
