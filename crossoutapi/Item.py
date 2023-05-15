

__all__ = ['Item']


class Item:

    def __init__(self, data: dict) -> None:
        self.id = data['id']