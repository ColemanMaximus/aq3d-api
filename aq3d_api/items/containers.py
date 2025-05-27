""" This module contains the Items class container. """

from aq3d_api.items.item import Item
from aq3d_api.api.updater import APIUpdater
from aq3d_api.api.handler import send_req_items


class Items(APIUpdater):
    """
    Items container class to bundle items together.
    Supports the APIUpdater class.
    """

    api_bulk_req_limit = 200

    def __init__(self,
                 items = None,
                 fromapi: bool = False,
                 api_items_min: int = 1,
                 api_items_max: int = 1,
                 auto_update_fromapi: bool = False,
                 update_interval: int = 60
                 ):

        """
        :param items: The items which should be added to the container of initialization.
        :param fromapi: Should items be fetched from the official API.
        :param api_items_min: The start index for item IDs to be fetched.
        :param api_items_max: The end index for item IDs to be fetched.
        :param auto_update_fromapi: If items data should be refreshed after the update interval.
        :param update_interval: After how many seconds until new item data should be fetched.
        """

        self.items = items
        self.api_item_min = api_items_min
        self.api_item_max = api_items_max

        if fromapi:
            self.items = self.__fetch_fromapi()

        super().__init__(auto_update_fromapi, update_interval)

    def __fetch_fromapi(self) -> list | None:
        """
        Requests items to be fetched from the official API.

        :return: The fetched items as a list of Item objects.
        """

        raw_items = send_req_items(self.api_item_min, self.api_item_max)
        items = [Item.create_raw(item) for item in raw_items]

        return items

    def __iter__(self) -> iter:
        return iter(self.items)
