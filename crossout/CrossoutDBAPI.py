import urllib.parse

import requests


__all__ = ['CrossoutDBAPI']


class CrossoutDBAPI:
    """
    Low-level class that retrieves raw data as JSON from the CrossoutDB API.
    """

    def __init__(self, base_url : str = 'https://crossoutdb.com/api/v1/') -> None:
        """Build a `CrossoutDBAPI` object.

        Parameters
        ----------
        base_url : `str`, optional
            Base URL of the web API, should not be modified unless the API changes
        """
        self.base_url = base_url
        """Base URL of the web API, should not require modifications
        """

    def request(self, endpoint: str) -> set[dict]:
        """Makes a request to the CrossoutDB API and returns the result in JSON format.

        Parameters
        ----------
        endpoint : `str`
            Name of the endpoint to request

        Returns
        -------
        `set[dict]`
            A set of dicts retrieved from the CrossoutDB API. The set contains at least one dict.

        Raises
        ------
        `HTTPError`
            If the request failed
        `TypeError`
            If the response is not JSON
        """
        r = requests.get(self.base_url + endpoint)
        r.raise_for_status()
        
        s = set()
        if isinstance((resp := r.json()), dict):
            s.add(resp)
        elif isinstance(resp, list):
            for i in resp:
                s.add(i)
        else:
            raise TypeError(f'Invalid response: {resp}')
        return s

    def items(self,
            rarity: str | None = None,
            category: str | None = None,
            faction: str | None = None,
            query: str | None = None
        ) -> set[dict]:
        """Queries the CrossoutDB API for corresponding items by building an endpoint with GET parameters.

        Parameters
        ----------
        rarity : `str`, optional
            Filters by rarity name as listed in `rarities()`
        category : `str`, optional
            Filters by category name as listed in `categories()`
        faction : `str`, optional
            Filters by faction name as listed in `factions()`
        query : `str`, optional
            Filters items corresponding to the given query

        Returns
        -------
        `set[dict]`
            The list of items returned by the API
        """
        params = {}

        def addParameter(key: str, value: str | None, restrictedValues: list[str]) -> None:
            if value in restrictedValues:
                params[key] = value

        addParameter('rarity', rarity, [r['name'] for r in self.rarities()])
        addParameter('category', category, [c['name'] for c in self.categories()])
        addParameter('faction', faction, [f['name'] for f in self.factions()])

        if query:
            params['query'] = query

        return self.request('items?' + urllib.parse.urlencode(params))

    def item(self, item_id: int) -> dict:
        """Returns the item with the given ID.

        Parameters
        ----------
        item_id : `int`
            ID of the item to retrieve

        Returns
        -------
        `dict`
            A dict containing the item data

        Raises
        ------
        `ValueError`
            If the item with the given ID does not exist
        """
        data = self.request('item/' + str(item_id))
        assert (l := len(data)) <= 1
        if l == 0:
            raise ValueError('Item with ID '+ str(item_id) +' does not exist.')
        return data.pop()
    
    def rarities(self) -> set[dict]:
        """Queries the CrossoutDB API for all available rarities.

        Returns
        -------
        `set[dict]`
            The set of rarities
        """
        return self.request('rarities')
    
    def categories(self) -> set[dict]:
        """Queries the CrossoutDB API for all available item categories.

        Returns
        -------
        `set[dict]`
            The set of item categories
        """
        return self.request('categories')

    def factions(self) -> set[dict]:
        """Queries the CrossoutDB API for all available factions.

        Returns
        -------
        `set[dict]`
            The set of factions
        """
        return self.request('factions')
    
    def types(self) -> set[dict]:
        """Queries the CrossoutDB API for all available item types.

        Returns
        -------
        `set[dict]`
            The set of item types
        """
        return self.request('types')
    
    def recipe(self, item_id: int) -> dict:
        """Queries the CrossoutDB API for the given item's recipe.

        Parameters
        ----------
        item_id : `int`
            ID of the item's recipe to retrieve

        Returns
        -------
        `dict` 
            A containing the recipe data

        Raises
        ------
        `ValueError`
            If the recipe with the given ID does not exist
        """
        # Empty JSON response
        if len(data := self.request('recipe/' + str(item_id))) <= 0:
            raise ValueError('Recipe with ID '+ str(item_id) +' does not exist.')
        
        data = data.pop()["recipe"]
        
        # Recipe data with no ingredients
        if len(data["ingredients"]) <= 0:
            raise ValueError('Recipe with ID '+ str(item_id) +' does not exist.')
        
        return data