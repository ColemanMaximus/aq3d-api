"""
This module provides the Maps container class for managing and interacting with collections of Map objects.
It includes functionality to fetch map data from the AQ3D API, and filter maps by key-value pairs.
"""

from collections.abc import Generator

from aq3d_api.api.handler import send_req_maps
from aq3d_api.api.service import APIService
from aq3d_api.containers.container import DataContainer
from aq3d_api.maps.map import Map


class Maps(DataContainer, APIService):
    def __init__(self, options: dict = {}):
        """
        ### Parameters:
            **auto-update (bool)**: Whether to automatically update maps from the API.
            **min-index (int)**: Minimum number of maps by ID range.
            **max-index (int)**: Maximum number of maps by ID range.
            **update-interval (int)**: Interval (in seconds) for automatic updates.

        ### Example
        ```
        {
            "auto-update": True,
            "min-index": 1,
            "max-index": 10,
            "update-interval": 1000
        }
        ```
        """


        DataContainer.__init__(self)
        APIService.__init__(self, options)

    @property
    def maps(self) -> list[Map]:
        """
        Returns a list of all available Map objects after updating
        the internal state.
        """

        self.update()
        return list(self._objs)

    def maps_by_keypair(self, key: str, value) -> Generator[Map]:
        """
        Yields all Map objects where the specified attribute (key) exists.

        ### Parameters:
            **key (str)**: The attribute name to look for in each Map object.
            **value (_type_)**: The expected value for the specified attribute.

        ### Raises:
            **ValueError**: If key is not a string.
            **ValueError**: If value is empty or None.

        ### Yields:
            **Generator[Map]**: Yields Map objects that have the specified attribute
        """


        if not isinstance(key, str):
            raise ValueError("Expected a string of a maps key.")

        if not value:
            raise ValueError("Expected a non empty value for keys value.")

        return (map for map in self.maps if map.__getattribute__(key))

    def _fetch(self) -> tuple:
        """
        Returns a tuple containing the current container, the send_req_maps function,
        and the Map class.
        """

        return tuple([self, send_req_maps, Map])

    def __getitem__(self, index: int) -> Map:
        return self.maps[index]

    def __iter__(self) -> Generator:
        return (map for map in self.maps)
