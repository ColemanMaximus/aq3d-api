"""
This module provides the APIUpdater base class, which manages automatic updating of locally cached data from an external API.
It defines the interface and logic for checking update intervals and fetching fresh data, intended to be extended by subclasses.
"""

from time import time
from abc import abstractmethod

class APIUpdater:
    """
    APIUpdater is a base class for managing periodic updates of cached data from an API.
    It provides logic to determine when data needs refreshing based on a configurable interval,
    and defines an interface for fetching new data from the API.
    Subclasses should implement the __fetch_fromapi method with specific retrieval logic.
    """

    def __init__(self, auto_update_fromapi: bool, update_interval: int):
        """"
        Parameters:
            auto_update_fromapi (bool): If True, enables automatic updates from the API.
            update_interval (int): The interval in seconds between update checks.
        """

        self._auto_update = auto_update_fromapi
        self._update_interval = update_interval
        self._last_updated = time()

    @property
    def __needs_updating(self) -> bool:
        """
        Checks if the updater needs to perform an update based on the elapsed
        time since the last update.

        Returns:
            bool: If the time since the last update exceeds the update interval.
        """

        if (time() - self._last_updated) < self._update_interval:
            return False

        return True

    def _update_fromapi(self) -> tuple | None:
        """
        Fetches and updates data from the API if an update is needed.

        Returns:
            tuple: The data fetched from the API as a tuple.
        """

        if not self.__needs_updating:
            return None

        self._last_updated = time()
        return self.__fetch_fromapi()

    @abstractmethod
    def __fetch_fromapi(self) -> tuple | None:
        """
        Fetches data from the API.

        Returns:
            tuple: A tuple containing the fetched data.

        Notes:
            Subclasses should implement this method and their own retrieval logic.
        """


        pass
