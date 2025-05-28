""" This module contains the Dialogs class. """

from collections.abc import Generator

from aq3d_api.api.handler import send_req_dialogs
from aq3d_api.api.updater import APIUpdater
from aq3d_api.containers.container import DataContainer
from aq3d_api.dialogs.dialog import Dialog


class Dialogs(DataContainer, APIUpdater):
    """
    This class wraps a bundle of Dialog objects together.
    """

    def __init__(self,
                 dialogs = None,
                 fromapi: bool = False,
                 api_dialogs_min: int = 1,
                 api_dialogs_max: int = 1,
                 auto_update_fromapi: bool = False,
                 update_interval: int = 1000):

        """
        :param dialogs: If any dialogs should be added at initialization.
        :param fromapi: Whether dialogs should be fetched from the API.
        :param api_dialogs_min: The starting index for fetching dialogs.
        :param api_dialogs_max: The end index for fetching dialogs.
        :param auto_update_fromapi: Should the dialogs be updated after
        the update interval expires.
        :param update_interval: After how many seconds should fresh dialog
        data be fetched from the API.
        """

        self.dialogs = dialogs
        self.__api_dialog_min = api_dialogs_min
        self.__api_dialog_max = api_dialogs_max

        if fromapi:
            self.dialogs = self.__fetch_fromapi()

        super().__init__(auto_update_fromapi, update_interval)


    @property
    def dialogs(self) -> Generator[Dialog]:
        """
        Gets all the dialogs within this container.

        :return: Returns a generator of Dialog objects.
        """

        return self._objs

    @dialogs.setter
    def dialogs(self, dialogs = None):
        """
        Sets the Dialog objects which should be contained within this object.

        :param dialogs: The dialogs to be containerized.
        """

        if not dialogs:
            self._objs = dialogs
            return

        self._objs = [
            dialog for dialog in dialogs if isinstance(dialog, Dialog)
        ]

    def __fetch_fromapi(self) -> tuple | None:
        """
        Gets all dialogs from the official AQ3D API.

        :return tuple: A tuple of dialog objects.
        """

        raw_dialogs = (
            send_req_dialogs(self.__api_dialog_min, self.__api_dialog_max)
        )
        return tuple(
            Dialog.create_raw(raw_dialog) for raw_dialog in raw_dialogs
        )
