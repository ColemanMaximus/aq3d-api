""" This module contains Enum class types for API Urls """

from enum import Enum

base_api_url = "https://game.aq3d.com/api/Game"


class APIURLS(Enum):
    """
    The Enum class for API URLs.
    """

    GET_ITEMS = f"{base_api_url}/GetItems", "IDs"
    GET_SERVERS = f"{base_api_url}/GetServerList", ""
