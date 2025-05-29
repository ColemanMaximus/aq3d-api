from aq3d_api.enums.endpoints import Endpoints
from aq3d_api.api.requests import req_range

def get_items(min_index: int = 1,
                   max_index: int = 1,
                   bulk_max: int = 200) -> list:

    """
    Sends a request to the API to fetch a range of items
    from their IDs.

    :param min_index: The start index for item IDs.
    :param max_index: The end index for item IDs.
    :param bulk_max: How many IDs there can be within each bulk request.
    :return: Returns a dict object of item data from JSON form.
    """

    url = Endpoints.GET_ITEMS.value[0]
    param_key = Endpoints.GET_ITEMS.value[1]

    return req_range(url, "POST", param_key, min_index, max_index, bulk_max)
