

__all__ = ['IDName']


class MetaIDName(type):

    def __iter__(self):
        yield self.__getattribute__('id'), self.__getattribute__('name')

class IDName(metaclass=MetaIDName):

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f'{self.id}-{self.name}'
    
    def __eq__(self, other) -> bool:
        if isinstance(other, IDName):
            return self.id == other.id and self.name == other.name
        else:
            return False
        
    