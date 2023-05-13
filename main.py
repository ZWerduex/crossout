import typing
import urllib.parse

import requests


__all__ = ['CrossoutAPI']


class CrossoutAPI:

    def __init__(self) -> None:
        self.base_url = 'https://crossoutdb.com/api/v1/'

    def _request(self, endpoint: str) -> typing.Any:
        r = requests.get(self.base_url + endpoint)
        if r.status_code != 200:
            raise ConnectionError('Request failed with status code: ' + str(r.status_code))
        return r.json()

    def items(self, 
            rarity: str | None = None,
            category: str | None = None,
            faction: str | None = None,
            query: str | None = None
        ):
        getParameters = {}

        def addParameter(key: str, value: str | None, restrictedValues: list[str]) -> None:
            if value in restrictedValues:
                getParameters[key] = value

        addParameter('rarity', rarity, [r['name'] for r in self.rarities()])
        addParameter('category', category, [c['name'] for c in self.categories()])
        addParameter('faction', faction, [f['name'] for f in self.factions()])

        if query:
            getParameters['query'] = query

        return self._request('items?' + urllib.parse.urlencode(getParameters))

    def item(self, item_id: int) -> list:
        return self._request('item/' + str(item_id))
    
    def rarities(self) -> list:
        return self._request('rarities')
    
    def categories(self) -> list:
        return self._request('categories')

    def factions(self) -> list:
        return self._request('factions')
    
    def types(self) -> list:
        return self._request('types')
    
    def recipe(self, item_id: int, deep: bool = False) -> dict:
        return self._request('recipe' + ('-deep' if deep else '') + '/' + str(item_id))
    

if __name__ == '__main__':
    api = CrossoutAPI()
    print(api.items(faction = 'Hyperborea'))
