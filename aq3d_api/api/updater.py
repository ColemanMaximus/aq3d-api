"""
This module contains the classes which supports automatically updating
locally cached data from the official API.
"""

from time import time
from abc import abstractmethod

class APIUpdater:
    """
    Used for any directive containers which are configured
    to update its cached data every update interval in seconds.
    """

    def __init__(self, auto_update_fromapi: bool, update_interval: int):
        """
        :param auto_update_fromapi: Should the auto update pull from the API.
        :param update_interval: How long in seconds until fresh data
        has to be pulled from the API.
        """

        self._auto_update = auto_update_fromapi
        self._update_interval = update_interval
        self._last_updated = time()

    @property
    def __needs_updating(self) -> bool:
        """
        Checks whether the last updated time has expired based on
        the update interval.

        :return: A bool if new data needs to be fetched.
        """

        if (time() - self._last_updated) < self._update_interval:
            return False

        return True

    def _update_fromapi(self) -> tuple | None:
        """
        Calls the fetch method on the directives to retrieve fresh
        data from the API.

        :return: The retrieved data from the API.
        """

        if not self.__needs_updating:
            return None

        self._last_updated = time()
        return self.__fetch_fromapi()

    @abstractmethod
    def __fetch_fromapi(self) -> tuple | None:
        """
        The method which controls how to fetch data from the API.

        All directives should implement this and have
        its own logic.
        """

        pass