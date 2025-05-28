""" This module contains Enum class types for Endpoints """

from enum import Enum

base_api_url = "https://game.aq3d.com/api"


class Endpoints(Enum):
    """
    The Enum class for API URLs.
    """

    GET_SERVERS = f"{base_api_url}/Game/GetServerList", ""
    GET_ITEMS = f"{base_api_url}/Game/GetItems", "IDs"
    GET_MAPS = f"{base_api_url}/Game/GetDungeons", "IDs"
    GET_DIALOGS = f"{base_api_url}/Utilities/GetDialogueByID", "dialogueID"
