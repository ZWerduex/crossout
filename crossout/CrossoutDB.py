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
        s = self.api.items(
            rarity=rarity,
            category=category,
            faction=faction,
            query=query
        )
        for i in s:
            i['imagePath'] = self.api.website_url + i['imagePath']
        return list(Item(i) for i in s)
    
    def item(self, item_id: int) -> Item:
        i = self.api.item(item_id)
        i['imagePath'] = self.api.website_url + i['imagePath']
        return Item(i)
    
    def __buildEntityList(self, objects: list[dict]) -> list[Entity]:
        return list(Entity(o['id'], o['name']) for o in objects)

    def rarities(self) -> list[Entity]:
        return self.__buildEntityList(self.api.rarities())
    
    def categories(self) -> list[Entity]:
        return self.__buildEntityList(self.api.categories())

    def factions(self) -> list[Entity]:
        return self.__buildEntityList(self.api.factions())
    
    def types(self) -> list[Entity]:
        return self.__buildEntityList(self.api.types())
    
    def recipe(self, item: Item) -> Recipe:
        r = self.api.recipe(item.id)
        assert r['item']['id'] == item.id

        items = []
        resources = []
        workbench = Workbenches.fromRarityName(item.rarity.name)
        
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
