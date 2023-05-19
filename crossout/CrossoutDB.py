from .CrossoutDBAPI import CrossoutDBAPI
from .Item import Item
from .utils import IDName


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

    def factions(self) -> list[IDName]:
        return [IDName(f['id'], f['name']) for f in self.api.factions()]