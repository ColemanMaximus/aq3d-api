import requests
from requests import JSONDecodeError

from aq3d_api.items.item import Item
from aq3d_api.updater.api_updater import APIUpdater


class Items(APIUpdater):
    api_url = "https://game.aq3d.com/api/Game/GetItems"
    param_key = "IDs"
    api_bulk_req_limit = 200

    def __init__(self,
                 items = None,
                 fromapi: bool = False,
                 api_item_max: int = 0,
                 auto_update_fromapi: bool = False,
                 update_interval: int = 60
                 ):
        self.items = items
        self.api_item_max = api_item_max
        if fromapi:
            self.items = self.__fetch_fromapi()

        super().__init__(auto_update_fromapi, update_interval)

    def __fetch_fromapi(self) -> list | None:
        bulk_req_limit = self.api_bulk_req_limit
        item_limit = self.api_item_max

        get_reqs_needed = (
            (item_limit // bulk_req_limit), (item_limit % bulk_req_limit)
        )

        items = []
        max_iteration = get_reqs_needed[0]
        if get_reqs_needed[-1] > 0:
            max_iteration += 1

        for req_num in range(1, max_iteration + 1):
            start_index = (bulk_req_limit * (req_num - 1)) + 1\
                if req_num > 1 else 1

            end_index = (start_index + bulk_req_limit)
            if req_num >= max_iteration:
                end_index = (start_index + get_reqs_needed[-1])

            params = {self.param_key: [
                    key_id for key_id in range(start_index, end_index)
                ]
            }

            response = requests.post(self.api_url, params=params)
            try:
                raw_items = response.json()
                items += [Item.create_raw(item) for item in raw_items]
            except JSONDecodeError:
                raise JSONDecodeError(
                    "Invalid item data was retrieved from the api."
                )

        return items

    def __iter__(self) -> iter:
        return iter(self.items)