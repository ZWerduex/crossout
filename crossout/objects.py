

__all__ = ['Entity', 'Item', 'Recipe', 'Resource', 'Workbenches']


class Entity:
    """Represents an entity with an ID and a name. Used for rarities, categories, factions and types.
    """

    def __init__(self, id: int, name: str) -> None:
        """Builds an entity with the given ID and name

        Parameters
        ----------
        id : `int`
            The entity's ID
        name : `str`
            The entity's name
        """
        self.__id = id
        self.__name = name

    def __str__(self) -> str:
        return self.__name
    
    def __repr__(self) -> str:
        return str(self.__dict__)
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Entity):
            return self.__id == other.__id and self.__name == other.__name
        else:
            return False
        
    @property
    def id(self) -> int:
        """Returns the entity's ID

        Returns
        -------
        `int`
            The entity's ID
        """
        return self.__id
    
    @property
    def name(self) -> str:
        """Returns the entity's name

        Returns
        -------
        str
            The entity's name
        """
        return self.__name

class Item:
    """Represents an item in Crossout.
    """

    def __init__(self, data: dict) -> None:
        """Builds an item from the given data. 
        An item should not be built manually and rather be retrieved from the `CrossoutDB` class.
        """
        self.id = data['id']
        self.name = data['name']
        self.description = d if (d := data['description']) else "Not provided."

        self.rarity = Entity(data['rarityId'], data['rarityName'])
        self.category = Entity(data['categoryId'], data['categoryName'])
        self.type = Entity(data['typeId'], data['typeName'])
        self.faction = Entity(data['factionNumber'], data['faction'])

        self.img = data['imagePath']

    def __repr__(self) -> str:
        return str(self.__dict__)

class Resource:

    def __init__(self, data: dict) -> None:
        self.id = data['id']
        self.name = data['name'].replace(' x100', '')
        self.description = d if (d := data['description']) else "Not provided."

        self.img = data['imagePath']

    def __repr__(self) -> str:
        return str(self.__dict__)

class Workbench:

    def __init__(self, price: int, name: str) -> None:
        self.price = price
        self.name = name

    @property
    def fullName(self) -> str:
        return f'{self.name} Workbench'

class Workbenches:

    COMMON = Workbench(0, 'Common')
    RARE = Workbench(3, 'Rare')
    SPECIAL = Workbench(6, 'Special')
    EPIC = Workbench(15, 'Epic')
    LEGENDARY = Workbench(75, 'Legendary')
    RELIC = Workbench(0, 'Relic')

    @staticmethod
    def fromName(name: str) -> Workbench:
        l = [
            Workbenches.COMMON,
            Workbenches.RARE,
            Workbenches.SPECIAL,
            Workbenches.EPIC,
            Workbenches.LEGENDARY,
            Workbenches.RELIC
        ]
        for w in l:
            if w.name == name:
                return w
        raise ValueError(f'No workbench with name {name}')

class Recipe:

    def __init__(self,
                 items: list[tuple[Item, int]],
                 resources: list[tuple[Resource, int]],
                 workbench: Workbench,
                 faction: Entity
                ) -> None:
        self.items = items
        self.resources = resources
        self.workbench = workbench
        self.faction = faction

    def __repr__(self) -> str:
        return str(self.__dict__)