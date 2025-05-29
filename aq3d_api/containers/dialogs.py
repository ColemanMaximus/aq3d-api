"""
This module defines the Dialogs container class for managing collections of Dialog objects,
including support for fetching and updating dialog data from the AQ3D API.
"""

from collections.abc import Generator

from aq3d_api.api.handler import send_req_dialogs
from aq3d_api.api.service import APIService
from aq3d_api.containers.container import DataContainer
from aq3d_api.dialogs.dialog import Dialog


class Dialogs(DataContainer, APIService):
    """
    A container class for managing Dialog objects, with
    optional API integration.
    """

    def __init__(self, options: dict = {}):
        """
        ### Parameters:
            **auto_update (bool)**: Whether to automatically update dialogs from the API.
            **min_index (int)**: Minimum number of dialogs by ID range.
            **max_index (int)**: Maximum number of dialogs by ID range.
            **update_interval (int)**: Interval (in seconds) for automatic updates.

        ### Example
        ```
        {
            "auto-update": True,
            "min-index": 1,
            "max_index": 10,
            "update-interval": 1000
        }
        ```
        """

        DataContainer.__init__(self)
        APIService.__init__(self, options)


    @property
    def dialogs(self) -> list[Dialog]:
        """
        Returns the dialogs associated with this container.

        ### Returns:
            **list[Dialog]**: An iterator over Dialog objects contained within
            this instance.
        """

        # Need to make sure to update or check for updates when dialogs
        # are fetched.
        self.update()
        return list(self._objs)

    def _fetch(self) -> tuple:
        """
        Fetches and returns a tuple containing the current instance,
        the send_req_dialogs function, and the Dialog class.

        ### Returns:
            **tuple**: A tuple of the form (self, send_req_dialogs, Dialog)
        """

        return tuple((self, send_req_dialogs, Dialog))

    def __getitem__(self, index: int) -> Dialog:
        return self.dialogs[index]

    def __iter__(self) -> Generator:
        return (dialog for dialog in self.dialogs)
