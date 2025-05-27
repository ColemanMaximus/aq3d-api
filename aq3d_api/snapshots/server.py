""" This module contains the ServerSnapshot class. """

from aq3d_api.snapshots.snapshot import Snapshot

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
