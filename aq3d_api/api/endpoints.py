"""Enumeration of AQ3D API endpoint URLs and their required parameters."""

from enum import Enum

base_api_url = "https://game.aq3d.com/api"


class Endpoints(Enum):
    """
    Enumeration of API endpoints for the AQ3D API.

    Parameters:
        GET_SERVERS: Endpoint to retrieve the list of game servers.
        GET_ITEMS: Endpoint to retrieve item details by IDs.
        GET_MAPS: Endpoint to retrieve dungeon/map details by IDs.
        GET_DIALOGS: Endpoint to retrieve dialogue by dialogueID.
    """

    GET_SERVERS = f"{base_api_url}/Game/GetServerList", ""
    GET_ITEMS = f"{base_api_url}/Game/GetItems", "IDs"
    GET_MAPS = f"{base_api_url}/Game/GetDungeons", "IDs"
    GET_DIALOGS = f"{base_api_url}/Utilities/GetDialogueByID", "dialogueID"
