"""
This module defines the Servers class, which manages a collection of AQ3D server objects.
It provides methods and properties to access, filter, sort, and snapshot server data,
as well as aggregate statistics such as total online players.
"""

from collections.abc import Generator
from requests import JSONDecodeError

from aq3d_api.api.handlers.types import Handlers
from aq3d_api.api.service import APIService
from aq3d_api.containers.container import DataContainer
from aq3d_api.servers.server import Server
from aq3d_api.snapshots.server import ServerSnapshot

class Servers(DataContainer, APIService):
    """
    A container for managing AQ3D server objects.

    The Servers class provides methods and properties to access, filter, sort,
    and snapshot server data, as well as retrieve player statistics across all servers.
    """

    def __init__(self, options: dict = {}):
        """
        ### Parameters:
            **auto-update (bool)**: Whether to automatically servers maps from the API.
            **update-interval (int)**: Interval (in seconds) for automatic updates.

        ### Example
        ```
        {
            "auto-update": True,
            "update-interval": 60
        }
        ```
        """

        DataContainer.__init__(self)
        APIService.__init__(self, options)

    @property
    def servers(self) -> list[Server]:
        """
        Returns a list of Server objects after updating the internal state.

        ### Returns
            **list[Server]**: A List of Server instances from the container.
        """

        self.update()
        return list(self._objs)

    @property
    def online_servers(self) -> list[Server]:
        """
        Returns a list of servers that are currently online.

        ### Returns:
            **list[Server]**: A list of Server instances that are online.
        """

        return [server for server in self.servers if server.is_online]

    @property
    def total_players(self) -> int:
        """
        Returns a total number of players currently online
        across all servers.

        ### Returns:
            **int**: Total number of players online across all servers.
        """

        if not self.servers:
            return 0

        return sum([server.players for server in self.servers])

    def sorted_servers(self, reverse: bool = True, online: bool = False) -> list[Server]:
        """
        Returns a list of Server objects sorted by the number of players.

        ### Parameters:
            **reverse (bool, optional)**: Sorts the servers in descending order by player counts.
            **online (bool, optional)**: Only includes servers that are currently online.

        ### Returns:
            **list[Server]**: A list of Server objects sorted by the number of players.
        """

        return [server for server in
                sorted(
                    self.servers if not online else self.online_servers,
                    key=lambda server: server.players,
                    reverse=reverse
                )
        ]

    @property
    def highest_population(self) -> Server | None:
        """
        Returns the server with the highest population among online servers.

        ### Returns
            **Server**: The online server with the highest population.

        """

        if not self.servers:
            return None

        try:
            return list(self.sorted_servers(online=True))[0]
        except IndexError:
            return None

    def create_snapshots(self, online_only: bool = True) -> Generator[ServerSnapshot]:
        """
        Creates snapshots of the current servers.

        Snapshots can be used for analytical purcposes to save server stats
        with timestamps.

        ### Parameters:
            **online_only (bool, optional)**: Only include servers that are currently online.

        ### Yields:
            **Generator[ServerSnapshot]**: A snapshot object representing the state of each server.
        """

        snapshots = (
            ServerSnapshot(server)
            for server in self.sorted_servers(online=online_only)
        )
        return snapshots

    def _fetch(self) -> tuple:
        """
        Returns a tuple containing the current container, the Handlers.SERVERS handler,
        and the Server class.
        """

        return tuple([self, Handlers.SERVERS, Server]) # type: ignore

    def __str__(self):
        response = \
            f"Servers ({len(self.servers)}): Players -> {self.total_players}"

        for server in self.servers:
            response += f"\n  - {server}"

        return response
