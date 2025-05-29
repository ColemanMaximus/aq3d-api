from aq3d_api.api.endpoints import Endpoints
from aq3d_api.api.requests import req_range


def get_maps(min_index: int = 1,
                   max_index: int = 1,
                   bulk_max: int = 200) -> list:

    """
    Sends a request to the API to fetch a range of maps
    from their IDs.

    :param min_index: The start index for map IDs.
    :param max_index: The end index for map IDs.
    :param bulk_max: How many IDs there can be within each bulk request.
    :return: Returns a dict object of map data from JSON form.
    """

    url = Endpoints.GET_MAPS.value[0]
    param_key = Endpoints.GET_MAPS.value[1]

    # We return index 0 because maps are structured as a dict rather than a list of dicts.
    return req_range(url, "POST", param_key, min_index, max_index, bulk_max)[0]
