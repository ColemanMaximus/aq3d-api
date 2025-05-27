""" This module contains the base class for Snapshot derivatives. """

from time import time
from abc import ABC

class Snapshot(ABC):
    """
    The snapshot class is an abstract interface for capturing
    a copy of an objects structure, including a timestamp of snapshot.
    """

    def __init__(self, obj: object):
        """
        :param obj: The object which should be captured as a snapshot.
        """

        self.__dict = {
            key.split("__")[-1]: value
            for key, value in tuple(obj.__dict__.items())
        }
        self.__timestamp = time()

    @property
    def _dict(self):
        """
        Protected property for accessing the dict of
        the snapshotted data.

        :return: Returns the dict of the snapshotted object.
        """

        return self.__dict

    @property
    def timestamp(self) -> float:
        """
        Returns the timestamp since epoch of when
        the snapshot was created.

        :return: Returns the timestamp in epoch.
        """

        return self.__timestamp

    def __getitem__(self, key):
        return self._dict[key]
