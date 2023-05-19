

__all__ = ['Entity', 'Item', 'Recipe', 'Resource']


class Entity:

    def __init__(self, id: int, name: str) -> None:
        self.__id = id
        self.__name = name

    def __str__(self) -> str:
        return self.__name
    
    def __repr__(self) -> str:
        return str(self.__dict__)
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Entity):
            return self.__id == other.id and self.__name == other.__name
        else:
            return False
        
    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def name(self) -> str:
        return self.__name

class Item:

    def __init__(self, data: dict) -> None:
        self.id = data['id']
        self.name = data['name']
        self.description = d if (d := data['description']) else "Not provided."

        self.rarity = Entity(data['rarityId'], data['rarityName'])
        self.category = Entity(data['categoryId'], data['categoryName'])
        self.type = Entity(data['typeId'], data['typeName'])
        self.faction = Entity(data['factionNumber'], data['faction'])

        self.imagePath = data['imagePath']

    def __repr__(self) -> str:
        return str(self.__dict__)

class Resource:

    def __init__(self, data: dict) -> None:
        self.id = data['id']
        self.name = data['name'].replace(' x100', '')
        self.description = d if (d := data['description']) else "Not provided."

        self.imagePath = data['imagePath']

    def __repr__(self) -> str:
        return str(self.__dict__)

class Recipe:

    def __init__(self,
                 items: list[tuple[Item, int]],
                 ressources: list[tuple[Resource, int]],
                 price: int
                ) -> None:
        self.items = items
        self.ressources = ressources
        self.price = price

    def __repr__(self) -> str:
        return str(self.__dict__)