""" This module contains classes and functions for capturing server metadata."""

import requests

from datetime import datetime
from time import time
from enum import Enum
from json import JSONDecodeError

from aq3d_api.snapshots import Snapshot


class ServerStatus(Enum):
    """
    An Enum of server status codes, from ONLINE, OFFLINE,
    and MAINTENANCE.
    """

    MAINTENANCE = "2"
    ONLINE = "1",
    OFFLINE = "0"


class ServerSnapshot(Snapshot):
    """
    Captures a snapshot of a Server instance.

    Useful for snapshot logging to external databases.
    """

    def __init__(self, server):
        """
        :param server: The server in which the snapshot should target.
        """

        if not isinstance(server, Server):
            raise ValueError("Was expecting an instance of Server for the snapshots.")

        super().__init__(server)

    @property
    def server_data(self) -> dict:
        """
        Returns a dict representation of a Server object structure.
        Access data using scriptable keys.

        :return: Returns a dict of server metadata.
        """

        return self._dict


class Server:
    """ Metadata about a server is bundled up into this Server class. """

    maintenance_buffer = 10

    def __init__(self,
                 id: int,
                 name: str,
                 region: str = "NA",
                 language: str = "en",
                 players: int = 0,
                 max_players: int = 0,
                 hostname: str = "",
                 port: int = 0,
                 access_level: int = 0,
                 status: ServerStatus = ServerStatus.OFFLINE,
                 last_updated: float = -1
                 ):
        """

        :param id: ID of the server.
        :param name: The servers name.
        :param region: Region areacode for the server.
        :param language: Language of the server.
        :param players: How many players are online.
        :param max_players: The maximum amount of players this server can hold.
        :param hostname: The hostname the server operates on.
        :param port: The port number the server listens to.
        :param access_level: The access or permission level for the server.
        :param status: The server uptime indicator, ONLINE, OFFLINE AND MAINTENANCE.
        """

        self.id = id
        self.name = name
        self.region = region
        self.language = language
        self.players = players
        self.max_players = max_players
        self.hostname = hostname
        self.port = port
        self.access_level = access_level
        self.status = status
        self.last_updated = last_updated

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        if not id or not isinstance(id, int):
            raise ValueError("Invalid id for the server was provided.")

        self.__id = id

    @property
    def name(self) -> str:
        """
        Returns the name of the server.

        :return str: The name of the server.
        """

        return self.__name

    @name.setter
    def name(self, name: str):
        """
        Sets the name of the server.

        Server names can't be an empty value, they require
        a valid non-empty string.

        :param name: The name the server should have.
        """

        if not isinstance(name, str) or not name.strip():
            raise ValueError("None/invalid name was provided for the server.")

        # Some server names have the regions areacode attached to the name,
        # this will filter them so only the name itself is used.
        if "[" in name:
            name = name.split("[")[0].strip()

        self.__name = name

    @property
    def region(self) -> str:
        """
        Returns an areacode for the region in which the server
        is based in.

        :return str: Areacode for the region.
        """

        return self.__region

    @region.setter
    def region(self, region: str):
        """
        Sets the regions areacode for the server. Such as NA, SEA, EU...

        :param region: The regions areacode.
        """

        if not isinstance(region, str):
            raise ValueError(
                "Expected a string region areacode for the servers region."
            )

        self.__region = region.upper()

    @property
    def language(self) -> str:
        """
        Returns the language of the server.

        :return str: The language of the server.
        """

        return self.__language

    @language.setter
    def language(self, lang):
        """
        Sets the language of the server, such as en.

        :param lang: The language the server targets.
        """

        if not isinstance(lang, str):
            raise ValueError("Expected a string for servers language.")

        self.__language = lang

    @property
    def players(self) -> int:
        """
        Returns the number of online players.

        :return int: Number of online players.
        """

        # Online servers themselves count towards player counts
        # so we negate 1 to avoid counting a fake player.
        return 0 if (self.__players <= 0) else (self.__players - 1)

    @players.setter
    def players(self, value: int):
        """
        Sets the number of players online to the value.

        :param value: The number of players online.
        """

        if not isinstance(value, int):
            raise ValueError("Expected an integer value.")

        self.__players = value

    @property
    def max_players(self) -> int:
        """
        Returns the maximum amount of players allowed on
        the server at once.

        :return int: Returns the maximum amount of players.
        """

        return self.__max_players

    @max_players.setter
    def max_players(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Invalid max players value provided. Expected an integer, or a positive number.")

        self.__max_players = value

    @property
    def hostname(self) -> str:
        """
        Returns the hostname which the server is using.

        :return: Servers hostname.
        """

        return self.__hostname

    @hostname.setter
    def hostname(self, hostname: str):
        """
        Sets the servers hostname to the one it's operating on.

        :param hostname: The hostname of the server.
        """

        if not isinstance(hostname, str):
            raise ValueError("Expected a string for the servers hostname.")

        self.__hostname = hostname

    @property
    def port(self) -> int:
        """
        Returns the servers port number which it's listening to.

        :return int: Servers port number.
        """

        return self.__port

    @port.setter
    def port(self, port: int):
        """
        Sets the port number which the server will operate on
        between 0 and 65535.


        :param port: THe port the server should listen on.
        """

        if not isinstance(port, int):
            raise ValueError("Expected an integer for the port number.")

        if not 0 <= port <= 65535:
            raise ValueError("Ports can only be between 0 and 65535.")

        self.__port = port

    @property
    def access_level(self) -> int:
        """
        Returns the access level of the server, which is a kind of
        permission level. 0 being player access, 100 admin access only.

        :return int: The access level as an integer.
        """

        return self.__access_level

    @access_level.setter
    def access_level(self, access_level: int):
        """
        Sets the access level for the server, which defines a permission
        access level.

        :param access_level: The access level in which the server holds.
        """

        if not isinstance(access_level, int):
            raise ValueError("Expected an integer for access level.")

        self.__access_level = access_level

    @property
    def status(self) -> ServerStatus:
        """
        Returns the status of the server, either
        ONLINE, OFFLINE OR MAINTENANCE.

        :return ServerStatus: Status of the server.
        """

        # When servers are in maintenance they usually have between 1 and 10
        # players, accounting for devs. So it's safe to say within this range
        # the server is likely in maintenance.
        if 1 <= self.players <= self.maintenance_buffer:
            return ServerStatus.MAINTENANCE

        return self.__status

    @status.setter
    def status(self, status: ServerStatus):
        """
        Sets the status for the server, which acts as an
        uptime indicator, 0 is offline, 1 is online.

        :param status: The status which can either be 0 or 1.
        """

        if not isinstance(status, ServerStatus):
            raise ValueError("Expected a ServerStatus for server status, either ONLINE, OFFLINE OR MAINTENANCE.")

        self.__status = status

    @property
    def last_updated(self) -> float:
        """
        Returns a timestamp of the last time the server
        data was refreshed.

        :return float: Timestamp of the last time the server was refreshed.
        """

        return self.__last_updated

    @last_updated.setter
    def last_updated(self, timestamp: float | int):
        """
        Sets the last update to a timestamp based on
        seconds since epoch.

        :param timestamp: The timestamp of the last time the server
        data was refreshed.
        """

        if not isinstance(timestamp, (float, int)):
            raise ValueError("Expected a timestamp of either a float or integer value.")

        self.__last_updated = timestamp

    @property
    def is_full(self) -> bool:
        """
        Returns a bool depending on if the server has reached
        or exceeded its player limit.

        :return bool: Returns bool based on player limits.
        """

        return self.players >= self.max_players

    @property
    def is_online(self) -> bool:
        """
        Returns a bool based on if the server is online or offline based
        on the servers status code.

        :return: Returns bool based on server status.
        """

        return self.status == ServerStatus.ONLINE

    def create_snapshot(self) -> ServerSnapshot:
        return ServerSnapshot(self)

    @classmethod
    def create_raw(cls, raw):
        """
        Factory method to return a Server object based on raw json
        structured as if it were from the official AQ3D API endpoint.

        :param raw: Expects raw json based on the structure of the servers AQ3D API.
        :return Server: Returns a Server object based on the raw json data.

        """

        return cls(
            id = raw.get("ID"),
            name = raw.get("Name"),
            region = raw.get("Region", "NA"),
            language = raw.get("Language", "en"),
            players = raw.get("UserCount", 0),
            max_players = raw.get("MaxUsers", 0),
            hostname = raw.get("HostName"),
            port = raw.get("Port", 0),
            access_level = raw.get("AccessLevel", 0),
            status = _statuscode_to_status(
                raw.get("Status", ServerStatus.OFFLINE)
            ),
            last_updated = datetime.strptime(
                raw.get("LastUpdated", ""), "%Y-%m-%dT%H:%M:%S"
            ).timestamp()
        )

    def __str__(self) -> str:
        online_status = self.status.name
        players = f"{self.players}/{self.max_players}"

        return f"({self.id}) {self.name} ({online_status}) -> {players}"


class Servers:
    """ A class bundle of related servers, and useful methods. """

    api_url = "https://game.aq3d.com/api/game/GetServerList"

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
        self.__last_updated = None

        if fromapi:
            self.servers = list(self.__fetch_servers_fromapi())
            self.__last_updated = time()

        self.__auto_update = auto_update_fromapi
        self.__update_interval = update_interval

    @property
    def servers(self) -> tuple:
        """
        Returns all servers within this Servers instance.
        
        :return tuple: A tuple of server objects.
        """

        if self.__auto_update:
            self.__update_servers_fromapi()

        return tuple(self.__servers)

    @servers.setter
    def servers(self, servers = None):
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

    @property
    def __needs_updating(self) -> bool:
        if (time() - self.__last_updated) < self.__update_interval:
            return False

        return True

    def __update_servers_fromapi(self):
        if not self.__needs_updating:
            return

        self.servers = self.__fetch_servers_fromapi()
        self.__last_updated = time()

    def __fetch_servers_fromapi(self) -> tuple | None:
        """
        Gets all servers from the official AQ3D API.

        :return tuple: A tuple of Server objects.
        """

        response = requests.get(self.api_url)
        if not response.ok:
            return None

        try:
            raw_servers = response.json()["Servers"]
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


def _statuscode_to_status(statuscode: int) -> ServerStatus:
    """
    Returns the ServerStatus representation of an integer status code.

    :param statuscode: An integer of the status code, 0 or 1.
    :return: Returns a ServerStatus representation of the status code.
    """

    if statuscode == 0:
        return ServerStatus.OFFLINE

    return ServerStatus.ONLINE
