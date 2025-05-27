""" This module contains then Servers container class. """
from collections.abc import Generator
from requests import JSONDecodeError

from aq3d_api.api.updater import APIUpdater
from aq3d_api.containers.container import DataContainer
from aq3d_api.servers.server import Server
from aq3d_api.snapshots.server import ServerSnapshot
from aq3d_api.api.handler import send_req_servers

class Servers(DataContainer, APIUpdater):
    """ A class bundle of related servers, and useful methods. """

    def __init__(self,
                 servers = None,
                 fromapi: bool = False,
                 auto_update_fromapi: bool = False,
                 update_interval: int = 60
                 ):
        """
        :param servers: Any Server objects to be added at initialization.
        :param fromapi: If true, the constructor will gather all servers
        from the official AQ3D API.
        :param auto_update_fromapi: If true, any time the servers property
        is called, it'll check to see if it needs refreshing based on the update
        interval class attribute.
        :param update_interval: How often should the auto update interval
        be in seconds.

        """

        self.servers = servers
        if fromapi:
            self.servers = list(self.__fetch_fromapi())

        super().__init__(auto_update_fromapi, update_interval)

    @property
    def servers(self) -> Generator[Server]:
        """
        Returns all servers within this Servers instance.

        :return: Generator of Server objects.
        """

        if self._auto_update:
            self._update_fromapi()

        return self._objs

    @servers.setter
    def servers(self, servers=None):
        """
        Sets the servers attribute to an initial sequence of servers.

        :param servers: The servers to add to this Servers instance.
        """

        if not servers:
            self._objs = servers
            return

        self._objs = [
            server for server in servers if isinstance(server, Server)
        ]

    @property
    def online_servers(self) -> Generator:
        """
        Gets all servers are on online, filtering offline
        and maintenance servers.

        :return: Returns a generator of online servers.
        """

        return (server for server in self.servers if server.is_online)

    def add(self, server: Server):
        """
        Adds a Server object into the Servers instance.

        :param server: The Server object to add into the Servers container.
        """

        if not isinstance(server, Server):
            raise ValueError(f"Expected a Server object but instead received {type(server)}.")

        if self.servers:
            servers = list(self._objs)
            servers.append(server)
            self.servers = servers

    @property
    def total_players(self) -> int:
        """
        Returns the number of online players across all servers.

        :return int: The number of online players.
        """

        if not self.servers:
            return 0

        return sum([server.players for server in self.servers])

    def sorted_servers(self, reverse: bool = True, online: bool = False) -> Generator[Server] | None:
        """
        Returns a sorted tuple of servers by player counts.

        :param reverse: If the sorted servers should be reversed.
        :param online: If the servers should only include online servers.
        :return: Returns a sorted tuple of servers, otherwise None.
        """

        return (server for server in
            sorted(
                self.servers if not online else self.online_servers,
                key=lambda server: server.players,
                reverse=reverse
            )
        )

    @property
    def highest_population(self) -> Server | None:
        """
        Returns the server which has the most online players.

        :return: The server with the most players online.
        """

        if not self.servers:
            return None

        return list(self.sorted_servers(online=True))[0]

    def create_snapshots(self, online_only: bool = True) -> Generator[ServerSnapshot]:
        """
        Generates a snapshot of each server assigned to this instance.

        :param online_only: Whether to only snapshot online servers or both.
        :return: Tuple of sever snapshots.
        """

        snapshots = (
            ServerSnapshot(server)
             for server in self.sorted_servers(online=online_only)
        )
        return snapshots

    def __fetch_fromapi(self) -> tuple | None:
        """
        Gets all servers from the official AQ3D API.

        :return tuple: A tuple of Server objects.
        """

        try:
            raw_servers = send_req_servers()["Servers"]
            return tuple(Server.create_raw(raw_server) for raw_server in raw_servers)
        except JSONDecodeError:
            raise ValueError("Invalid JSON was received from the api.")

    def __str__(self):
        response = \
            f"Servers ({len(list(self.servers))}): Players -> {self.total_players}"

        for server in self.servers:
            response += f"\n  - {server}"

        return response
