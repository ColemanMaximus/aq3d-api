from enum import Enum

class ServerStatus(Enum):
    """
    An Enum of server status codes, from ONLINE, OFFLINE,
    and MAINTENANCE.
    """

    MAINTENANCE = 2
    ONLINE = 1
    OFFLINE = 0