from aq3d_api.api.endpoints import Endpoints
from aq3d_api.api.requests import api_req

def get_servers() -> dict:
    """
    Sends a request to fetch all servers from the official API.

    :return: Returns the servers as a dict object.
    """

    return api_req(Endpoints.GET_SERVERS.value[0])
