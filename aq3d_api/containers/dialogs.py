"""
This module defines the Dialogs container class for managing collections of Dialog objects,
including support for fetching and updating dialog data from the AQ3D API.
"""

from collections.abc import Generator

from aq3d_api.api.handler import send_req_dialogs
from aq3d_api.api.updater import APIUpdater
from aq3d_api.containers.container import DataContainer
from aq3d_api.dialogs.dialog import Dialog


class Dialogs(DataContainer, APIUpdater):
    """
    A container class for managing Dialog objects, with optional API integration
    and auto-update functionality.
    """

    def __init__(self,
                 dialogs = None,
                 fromapi: bool = False,
                 api_dialogs_min: int = 1,
                 api_dialogs_max: int = 1,
                 auto_update_fromapi: bool = False,
                 update_interval: int = 1000):

        """
        Parameters:
            dialogs (optional): Initial dialogs to populate the container.
            fromapi (bool): Whether to fetch dialogs from the API.
            api_dialogs_min (int): Minimum number of dialogs to fetch from the API.
            api_dialogs_max (int): Maximum number of dialogs to fetch from the API.
            auto_update_fromapi (bool): Whether to automatically update dialogs from the API.
            update_interval (int): Interval (in seconds) for automatic updates.
        """

        self.dialogs = dialogs
        self.__api_dialog_min = api_dialogs_min
        self.__api_dialog_max = api_dialogs_max

        if fromapi:
            self.dialogs = self.__fetch_fromapi()

        DataContainer.__init__(self, dialogs)
        APIUpdater.__init__(self, auto_update_fromapi, update_interval)


    @property
    def dialogs(self) -> Generator[Dialog]:
        """
        Yields the dialogs associated with this container.

        Yields:
            Generator[Dialog]: An iterator over Dialog objects contained within this instance.
        """

        return self._objs

    @dialogs.setter
    def dialogs(self, dialogs = None):
        """
        Sets the internal dialogs list after validating each item.

        Parameters:
            dialogs (list[Dialog]): _description_. A list of Dialog objects to be assigned.
        """

        if not dialogs:
            self._objs = dialogs
            return

        self._objs = [
            dialog for dialog in dialogs if isinstance(dialog, Dialog)
        ]

    def __fetch_fromapi(self) -> tuple | None:
        """
        Fetches dialog data from the API and returns it as a tuple of Dialog objects.

        Returns:
            tuple[Dialog]: A tuple containing Dialog objects if dialogs are found,
        """

        raw_dialogs = (
            send_req_dialogs(self.__api_dialog_min, self.__api_dialog_max)
        )
        return tuple(
            Dialog.create_raw(raw_dialog) for raw_dialog in raw_dialogs
        )
