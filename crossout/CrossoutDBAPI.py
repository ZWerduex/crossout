import typing
import urllib.parse

import requests


__all__ = ['CrossoutDBAPI']


class CrossoutDBAPI:
    """
    Low-level class that retrieves raw data as JSON from the CrossoutDB API.
    """

    def __init__(self, base_url : str = 'https://crossoutdb.com/api/v1/') -> None:
        """Build the basic CrossoutAPI object.

        Parameters
        ----------
        base_url : str, optional
            Base URL of the web API, should not require modifications
        """
        self.base_url = base_url

    def request(self, endpoint: str) -> typing.Any:
        """Makes a request to the CrossoutDB API and returns the result in JSON format.

        Parameters
        ----------
        endpoint : str
            Name of the endpoint to request

        Returns
        -------
        typing.Any
            A dict or a list of dicts retrieved from the CrossoutDB API

        Raises
        ------
        HTTPError
            If the request failed
        """
        r = requests.get(self.base_url + endpoint)
        r.raise_for_status()
        return r.json()

    def items(self,
            rarity: str | None = None,
            category: str | None = None,
            faction: str | None = None,
            query: str | None = None
        ) -> list[dict]:
        """Queries the CrossoutDB API for corresponding items by building an endpoint with GET parameters.

        Parameters
        ----------
        rarity : str, optional
            Filters by rarity name as listed in `rarities()`
        category : str, optional
            Filters by category name as listed in `categories()`
        faction : str, optional
            Filters by faction name as listed in `factions()`
        query : str, optional
            Filters items corresponding to the given query

        Returns
        -------
        list[dict]
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
        item_id : int
            ID of the item to retrieve

        Returns
        -------
        dict
            A dict containing the item data

        Raises
        ------
        ValueError
            If the item with the given ID does not exist
        """
        data = self.request('item/' + str(item_id))
        assert (l := len(data)) <= 1
        if l == 0:
            raise ValueError('Item with ID '+ str(item_id) +' does not exist.')
        return data[0]
    
    def rarities(self) -> list[dict]:
        """Queries the CrossoutDB API for all available rarities.

        Returns
        -------
        list[dict]
            The list of rarities
        """
        return self.request('rarities')
    
    def categories(self) -> list[dict]:
        """Queries the CrossoutDB API for all available item categories.

        Returns
        -------
        list[dict]
            The list of item categories
        """
        return self.request('categories')

    def factions(self) -> list[dict]:
        """Queries the CrossoutDB API for all available factions.

        Returns
        -------
        list[dict]
            The list of factions
        """
        return self.request('factions')
    
    def types(self) -> list[dict]:
        """Queries the CrossoutDB API for all available item types.

        Returns
        -------
        list[dict]
            The list of item types
        """
        return self.request('types')
    
    def recipe(self, item_id: int) -> dict:
        """Returns the recipe for the given item.

        Parameters
        ----------
        item_id : int
            ID of the item's recipe to retrieve

        Returns
        -------
        dict 
            A containing the recipe data

        Raises
        ------
        ValueError
            If the recipe with the given ID does not exist
        """
        data = self.request('recipe/' + str(item_id))["recipe"]
        if len(data["ingredients"]) <= 0:
            raise ValueError('Recipe with ID '+ str(item_id) +' does not exist.')
        return data