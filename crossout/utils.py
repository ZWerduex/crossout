

__all__ = ['IDName']


class IDName:

    def __init__(self, id: int, name: str) -> None:
        self.__id = id
        self.__name = name

    def __str__(self) -> str:
        return self.__name
    
    def __repr__(self) -> str:
        return f'{self.__id}:{self.__name}'
    
    def __eq__(self, other) -> bool:
        if isinstance(other, IDName):
            return self.__id == other.id and self.__name == other.__name
        else:
            return False
        
    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def name(self) -> str:
        return self.__name
        
    