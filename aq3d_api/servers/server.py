""" This module contains the Server class. """
from datetime import datetime

from aq3d_api import utils
from aq3d_api.enums.server_status import ServerStatus
from aq3d_api.snapshots.server import ServerSnapshot

class Server:
    """ Metadata about a server is bundled up into a Server class. """

    maintenance_buffer = 10

    def __init__(self,
                 sid: int,
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

        :param sid: ID of the server.
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

        self.id = sid
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
    def id(self, sid: int):
        if not sid or not isinstance(sid, int):
            raise ValueError("Invalid id for the server was provided.")

        self.__id = sid

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
            sid = raw.get("ID"),
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

    def to_dict(self) -> dict:
        """
        Quickly converts the objects attributes to a dict.

        :return: The dict representation of the objects attributes.
        """

        return utils.to_dict(self)

    def __str__(self) -> str:
        online_status = self.status.name
        players = f"{self.players}/{self.max_players}"

        return f"({self.id}) {self.name} ({online_status}) -> {players}"

def _statuscode_to_status(statuscode: int) -> ServerStatus:
    """
    Returns the ServerStatus representation of an integer status code.

    :param statuscode: An integer of the status code, 0 or 1.
    :return: Returns a ServerStatus representation of the status code.
    """

    if statuscode == 0:
        return ServerStatus.OFFLINE

    return ServerStatus.ONLINE
