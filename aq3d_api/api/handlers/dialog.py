from aq3d_api.enums.endpoints import Endpoints
from aq3d_api.api.requests import req_range

def get_dialogs(min_index: int = 1,
                   max_index: int = 1,
                   bulk_max: int = 1) -> list:

    """
    Sends a request to the API to fetch a range of dialogs
    from their IDs.

    :param min_index: The start index for dialog IDs.
    :param max_index: The end index for dialog IDs.
    :param bulk_max: How many IDs there can be within each bulk request.
    :return: Returns a dict object of dialog data from JSON form.
    """

    url = Endpoints.GET_DIALOGS.value[0]
    param_key = Endpoints.GET_DIALOGS.value[1]

    raw_dialogs = (
        req_range(url, "GET", param_key, min_index, max_index, bulk_max)
    )

    return [dialog for dialog in raw_dialogs if dialog.get("ID", -1) > 0]
