"""
This module provides the APIService base class, which manages automatic updating of locally cached data from an external API.
It defines the interface and logic for checking update intervals and fetching fresh data, intended to be extended by subclasses.
"""

from time import time
from abc import abstractmethod

class APIService:
    """
    APIService is a base class for managing periodic updates of cached data from an API.
    It provides logic to determine when data needs refreshing based on a configurable interval,
    and defines an interface for fetching new data from the API.
    Subclasses should implement the `_fetch` method with specific retrieval logic.
    """

    def __init__(self, options: dict = {}):
        """
        ### Parameters:
            **auto-update (bool)**: Whether to automatically update dialogs from the API.
            **min-index (int)**: Minimum number of dialogs by ID range.
            **max-index (int)**: Maximum number of dialogs by ID range.
            **update-interval (int)**: Interval (in seconds) for automatic updates.
        """

        self._auto_update = options.get("auto-update", False)
        self._min_index = options.get("min-index", 1)
        self._max_index = options.get("max-index", 1)
        self._update_interval = options.get("update-interval", -1)
        self.__inital_update = False
        self._last_updated = time()

    @property
    def __needs_updating(self) -> bool:
        """
        Checks if the updater needs to perform an update based on the elapsed
        time since the last update.

        ### Returns:
            **bool**: If the time since the last update exceeds the update interval.
        """

        # At least the first update should gather data.
        if not self.__inital_update:
            return True

        # Shouldn't update if the value is -1, which means disabled.
        if self._update_interval <= -1:
            return False

        if (time() - self._last_updated) < self._update_interval:
            return False

        return True


    def update(self):
        """
        Fetches and updates data from the API if an update is needed.
        """

        if not self.__needs_updating:
            return None


        # The fetch method of the subclass will return a tuple
        # where the first part is the DataContainer subclass,
        # second is the type of handler to use to fetch the objects
        # from the API. The third the class type to create objects of.
        container, handler_func, cls = self._fetch()
        raw_objects = handler_func(self._min_index, self._max_index)

        if not raw_objects or not cls:
            return None

        self._last_updated = time()
        self.__inital_update = True

        # Some data from the API comes back as dict object rather than a list.
        # In this case make the values of that dict the list objects.
        if isinstance(raw_objects, dict):
            raw_objects = list(raw_objects.values())

        objects = [cls.create_raw(obj) for obj in raw_objects]

        # We need to overwrite the containers objects
        # to avoid duplication.
        container.append(cls, objects, True)

    @abstractmethod
    def _fetch(self) -> tuple:
        """
        Fetches data from the API.

        ### Returns:
            **tuple**: A tuple containing how to fetch and build the objects..

        ### Notes:
            Subclasses should implement this method and their own
            fetch return which describes how to build the object.

            - `return tuple((container, handler_func, containing_type))`
        """

        pass
