"""
This module contains functions to work with the API,
such as sending requests for servers and items.
"""

from requests import request, JSONDecodeError

def api_req(endpoint: str, method: str = "GET", params: dict = None) -> dict | None:
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


def req_range(url: str,
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

    difference = (max_index + 1) - min_index
    index_range_difference = difference if difference > 0 else 1

    requests_needed = (
        (index_range_difference // bulk_max),
        # The remainder of items remaining, used for
        # last second requests.
        (index_range_difference % bulk_max)
    )

    max_iteration = requests_needed[0]
    if requests_needed[-1] > 0:
        max_iteration += 1

    indices = []
    for req_index in range(1, max_iteration + 1):
        start_index = (bulk_max * (req_index - 1)) + 1 \
            if req_index > 1 else 1

        # We should begin the start index at the min value - 1
        # if the min value is above 1.
        if min_index > 1:
            start_index += min_index - 1

        end_index = (start_index + (bulk_max if bulk_max > 1 else 0))
        if req_index >= max_iteration:
            end_index = (start_index + requests_needed[-1])

        params = {param_key: [
            key_id for key_id in range(
                start_index, (end_index + 1)
                if end_index > 1 else 2
            )
        ]}

        response = api_req(url, method, params)
        if isinstance(response, dict):
            indices.append(response)
            continue

        if isinstance(response, list):
            indices += response

    return indices
