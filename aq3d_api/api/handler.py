"""
This module contains functions to work with the API,
such as sending requests for servers and items.
"""

from requests import request, JSONDecodeError
from aq3d_api.enums.urls import APIURLS


def send_api_req(endpoint: str, method: str = "GET", params: dict = None) -> dict | None:
    """
    Send an API request to an endpoint with custom
    method and params.

    :param endpoint: The URL to the API endpoint.
    :param method: Which HTTP method to use. GET, POST.
    :param params: Any parameters which should be passed with the request.
    :return: A dict representation of a JSON object.
    """

    try:
        response = request(method=method, url=endpoint, params=params)
        if not response.ok:
            return None

        return response.json()
    except JSONDecodeError:
        return None


def send_req_servers() -> dict:
    """
    Sends a request to fetch all servers from the official API.

    :return: Returns the servers as a dict object.
    """

    return send_api_req(APIURLS.GET_SERVERS.value[0])


def send_req_range(url: str,
                   method: str = "GET",
                   param_key: str = "",
                   min_index: int = 1,
                   max_index: int = 1,
                   bulk_max: int = 200) -> list:
    """
    :param url: The URL used to send an HTTP request to.
    :param method: Which HTTP method to use.
    :param param_key: The param key used to gather specific data.
    :param min_index: Where should the param key index start.
    :param max_index: Where should the param key index end.
    :param bulk_max: How many parameter key values can be added each request.
    :return: The result of the range of requests.
    """

    index_range_diff = max_index - min_index
    reqs_needed = (
        (index_range_diff // bulk_max),
        # The remainder of items remaining, used for
        # last second requests.
        (index_range_diff % bulk_max)
    )

    max_iteration = reqs_needed[0]
    if reqs_needed[-1] > 0:
        max_iteration += 1

    indices = []
    for req_num in range(1, max_iteration + 1):
        start_index = (bulk_max * (req_num - 1)) + 1 \
            if req_num > 1 else 1

        # We should begin the start index at the min value
        # if the min value is above 1.
        if min_index > 1:
            start_index += min_index

        end_index = (start_index + bulk_max)
        if req_num >= max_iteration:
            end_index = (start_index + reqs_needed[-1])

        params = {param_key: [
            key_id for key_id in range(start_index, end_index)
        ]}

        response = send_api_req(url, method, params)
        if isinstance(response, dict):
            indices += [indice[-1] for indice in response.items()]
            continue

        indices += send_api_req(url, method, params)
    return indices


def send_req_items(min_index: int = 1,
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

    url = APIURLS.GET_ITEMS.value[0]
    param_key = APIURLS.GET_ITEMS.value[1]

    return send_req_range(url, "POST", param_key, min_index, max_index, bulk_max)


def send_req_maps(min_index: int = 1,
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

    url = APIURLS.GET_MAPS.value[0]
    param_key = APIURLS.GET_MAPS.value[1]

    return send_req_range(url, "POST", param_key, min_index, max_index, bulk_max)
