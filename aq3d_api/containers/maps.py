""" This module contains the Maps class. """

from collections.abc import Generator

from aq3d_api.api.handler import send_req_maps
from aq3d_api.api.updater import APIUpdater
from aq3d_api.containers.container import DataContainer
from aq3d_api.maps.map import Map


class Maps(DataContainer, APIUpdater):
    def __init__(self,
                 maps = None,
                 fromapi: bool = False,
                 api_maps_min: int = 1,
                 api_maps_max: int = 1,
                 auto_update_fromapi: bool = False,
                 update_interval: int = 60
                 ):
        """
        :param maps: Map objects to be added at initialization.
        :param fromapi: If maps should be gathered from the official AQ3D API.
        :param api_maps_min: The start index for map IDs to be fetched.
        :param api_maps_max: The end index for map IDs to be fetched.
        :param auto_update_fromapi: If the map data should be updated
        after the update interval.
        :param update_interval: How long in seconds until the data expires, and
        ready for fresh data from the API.
        """

        self.maps = maps
        self.__api_maps_min = api_maps_min
        self.__api_maps_max = api_maps_max

        if fromapi:
            self.maps = self.__fetch_fromapi()

        DataContainer.__init__(self, maps)
        APIUpdater.__init__(self, auto_update_fromapi, update_interval)

    @property
    def maps(self) -> Generator[Map]:
        """
        Returns all maps within this Maps instance.

        :return generator: A generator of Map objects.
        """

        if self._auto_update:
            self._update_fromapi()

        return self._objs

    @maps.setter
    def maps(self, maps=None):
        """
        Sets the maps attribute to an initial list of maps.

        :param maps: The maps to add to this Maps instance.
        """

        if not maps:
            self._objs = maps
            return

        self._objs = [
            map for map in maps if isinstance(map, Map)
        ]

    def maps_by_keypair(self, key: str, value) -> Generator[Map]:
        """
        Returns a filtered list of Map objects if they have
        the matching key value pair.

        :param key: The key you want to filter by.
        :param value: The value the key should be to be considered a match.
        :return: A generator of filtered Map objects.
        """

        if not isinstance(key, str):
            raise ValueError("Expected a string of an maps key.")

        if not value:
            raise ValueError("Expected a non empty value for keys value.")

        return (map for map in self.maps if map.__getattribute__(key))

    def __fetch_fromapi(self) -> list | None:
        """
        Requests maps to be fetched from the official API.

        :return: The fetched maps as a list of Map objects.
        """

        raw_items = send_req_maps(self.__api_maps_min, self.__api_maps_max)
        return [Map.create_raw(item) for item in raw_items]
