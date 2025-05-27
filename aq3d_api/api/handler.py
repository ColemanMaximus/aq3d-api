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


def send_req_items(min_items: int = 1,
                   max_items: int = 1,
                   bulk_max: int = 200) -> list:

    """
    Sends a request to the API to fetch a range of items
    from their IDs.

    :param min_items: The start index for item IDs.
    :param max_items: The end index for item IDs.
    :param bulk_max: How many IDs there can be within each bulk request.
    :return: Returns a dict object of item data from JSON form.
    """

    url = APIURLS.GET_ITEMS.value[0]
    param_key = APIURLS.GET_ITEMS.value[1]

    item_range_diff = max_items - min_items
    reqs_needed = (
        (item_range_diff // bulk_max),
        # The remainder of items remaining, used for
        # last second requests.
        (item_range_diff % bulk_max)
    )

    max_iteration = reqs_needed[0]
    if reqs_needed[-1] > 0:
        max_iteration += 1

    items = []
    for req_num in range(1, max_iteration + 1):
        start_index = (bulk_max * (req_num - 1)) + 1 \
            if req_num > 1 else 1

        # We should begin the start index at the min value
        # if the min value is above 1.
        if min_items > 1:
            start_index += min_items

        end_index = (start_index + bulk_max)
        if req_num >= max_iteration:
            end_index = (start_index + reqs_needed[-1])

        params = {param_key: [
                key_id for key_id in range(start_index, end_index)
            ]
        }

        items += send_api_req(url, "POST", params)

    return items
