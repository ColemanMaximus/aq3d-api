""" This module contains Enum class types for Endpoints """

from enum import Enum

base_api_url = "https://game.aq3d.com/api/Game"


class Endpoints(Enum):
    """
    The Enum class for API URLs.
    """

    GET_SERVERS = f"{base_api_url}/GetServerList", ""
    GET_ITEMS = f"{base_api_url}/GetItems", "IDs"
    GET_MAPS = f"{base_api_url}/GetDungeons", "IDs"
