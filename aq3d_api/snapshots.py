"""
Module for snapshot related classes and functions,
for representing a copy of snapshotted object structures as a dict.
"""

from abc import ABC
from time import time

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


class ServerSnapshot(Snapshot):
    """
    Captures a snapshot of a Server instance.

    Useful for snapshot logging to external databases.
    """

    def __init__(self, server):
        """
        :param server: The server in which the snapshot should target.
        """

        super().__init__(server)

    @property
    def server_data(self) -> dict:
        """
        Returns a dict representation of a Server object structure.
        Access data using scriptable keys.

        :return: Returns a dict of server metadata.
        """

        return self._dict
