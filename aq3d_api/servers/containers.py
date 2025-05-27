""" This module contains then Servers container class. """

from requests import JSONDecodeError

from aq3d_api.api.updater import APIUpdater
from aq3d_api.servers.server import Server
from aq3d_api.snapshots.server import ServerSnapshot
from aq3d_api.api.handler import send_req_servers

class Servers(APIUpdater):
    """ A class bundle of related servers, and useful methods. """

    def __init__(self,
                 servers=None,
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
    def servers(self) -> tuple:
        """
        Returns all servers within this Servers instance.

        :return tuple: A tuple of server objects.
        """

        if self._auto_update:
            self._update_fromapi()

        return tuple(self.__servers)

    @servers.setter
    def servers(self, servers=None):
        """
        Sets the servers attribute to an initial sequence of servers.

        :param servers: The servers to add to this Servers instance.
        """

        if not servers:
            self.__servers = servers
            return

        self.__servers = [
            server for server in servers if isinstance(server, Server)
        ]

    @property
    def online_servers(self) -> tuple:
        """
        Gets all servers are on online, filtering offline
        and maintenance servers.

        :return tuple: Returns a tuple of online servers.
        """

        return tuple(server for server in self.servers if server.is_online)

    def add(self, server: Server):
        """
        Adds a Server object into the Servers instance.

        :param server: The Server object to add into the Servers container.
        """

        if not isinstance(server, Server):
            raise ValueError(f"Expected a Server object but instead received {type(server)}.")

        if self.servers:
            self.__servers.append(server)

    @property
    def total_players(self) -> int:
        """
        Returns the number of online players across all servers.

        :return int: The number of online players.
        """

        if not self.servers:
            return 0

        return sum([server.players for server in self.servers])

    def sorted_servers(self, reverse: bool = True, online: bool = False) -> tuple | None:
        """
        Returns a sorted tuple of servers by player counts.

        :param reverse: If the sorted servers should be reversed.
        :param online: If the servers should only include online servers.
        :return: Returns a sorted tuple of servers, otherwise None.
        """

        return tuple(
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

        return self.sorted_servers(online=True)[0]

    def create_snapshots(self, online_only: bool = True) -> tuple:
        """
        Generates a snapshot of each server assigned to this instance.

        :param online_only: Whether to only snapshot online servers or both.
        :return: Tuple of sever snapshots.
        """

        snapshots = tuple(
            [ServerSnapshot(server)
             for server in self.sorted_servers(online=online_only)]
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

    def __getitem__(self, index: int):
        if not isinstance(index, int):
            raise ValueError("Expected an index of the server.")

        return self.__servers[index]

    def __iter__(self) -> iter:
        return iter(self.servers)

    def __str__(self):
        response = \
            f"Servers ({len(self.servers)}): Players -> {self.total_players}"

        for server in self.servers:
            response += f"\n  - {server}"

        return response
