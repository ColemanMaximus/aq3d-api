"""
This module defines the Items container class for managing collections of Item objects.

It provides functionality to filter, update, and fetch items from the official API, supporting
various item attributes and types.
"""

from collections.abc import Generator

from aq3d_api.containers.container import DataContainer
from aq3d_api.items.item import Item
from aq3d_api.enums.item_type import ItemType
from aq3d_api.enums.item_equip_type import ItemEquipType
from aq3d_api.enums.item_rarity import ItemRarity
from aq3d_api.api.updater import APIUpdater
from aq3d_api.api.handler import send_req_items


class Items(DataContainer, APIUpdater):
    """
    A container class for managing and filtering collections of Item objects,
    with optional support for fetching and auto-updating items from an external API.
    """

    def __init__(self,
                 items = None,
                 fromapi: bool = False,
                 api_items_min: int = 1,
                 api_items_max: int = 1,
                 auto_update_fromapi: bool = False,
                 update_interval: int = 1000
                 ):

        """
        Parameters
            items (optional): Initial list of items.
            fromapi (bool): Whether to fetch items from the API.
            api_items_min (int): Minimum number of items to fetch from the API.
            api_items_max (int): Maximum number of items to fetch from the API.
            auto_update_fromapi (bool): Whether to automatically update items from the API.
            update_interval (int): Interval in seconds for automatic updates.
        """

        self.items = items
        self.__api_item_min = api_items_min
        self.__api_item_max = api_items_max

        if fromapi:
            self.items = self.__fetch_fromapi()

        DataContainer.__init__(self, items)
        APIUpdater.__init__(self, auto_update_fromapi, update_interval)

    @property
    def items(self) -> Generator[Item]:
        """
        Yields each Item object contained in the container.


        Yields:
            Generator[Item]: Item from the container.
        """

        return (item for item in self._objs)

    @items.setter
    def items(self, items):
        """
        Sets the internal list of item objects, filtering to include
        only instances of the `Item` class.

        Parameters:
            items (list): A list of objects to be filtered and stored.
        """

        if not items:
            self._objs = items
            return

        self._objs = [
            item for item in items if isinstance(item, Item)
        ]

    def items_by_type(self,
                      filter_type: ItemType
                                   | ItemEquipType
                                   | ItemRarity
                       ) -> Generator[Item]:
        """
        Yields items from the container that match the specified filter type.

        Depending on the type of `filter_type`, this method filters items by their rarity,
        equipment type, or item type.

        Parameters:
            filter_type (ItemType | ItemEquipType | ItemRarity): The item type to filter by.

        Yields:
            Generator[Item]: Items from the container that match the specified filter type
        """

        if isinstance(filter_type, ItemRarity):
            return (item for item in self.items if item.rarity == filter_type)
        if isinstance(filter_type, ItemEquipType):
            return (item for item in self.items if item.equip_type == filter_type)

        return (item for item in self.items if item.type == filter_type)

    def items_by_keypair(self, key: str, value) -> Generator[Item]:
        """
        Yields items from the container whose attribute `key` matches the specified `value`.

        Args:
            key (str): The name of the attribute to filter items by.
            value (Any): The value that the item's attribute should match.

        Raises:
            ValueError: If `key` is not a string.
            ValueError: If `value` is empty or None.


        Yields:
            Generator[Item]: Items whose attribute `key` equals `value`.
        """

        if not isinstance(key, str):
            raise ValueError("Expected a string of an items key.")

        if not value:
            raise ValueError("Expected a non empty value for keys value.")

        return (item for item in self.items if item.__getattribute__(key))

    def __fetch_fromapi(self) -> tuple | None:
        """
        Fetches item data from the API within the specified item ID range
        and returns a tuple of Item objects.

        Returns:
            tuple: A tuple containing Item instances created from the raw API response
        """

        raw_items = send_req_items(self.__api_item_min, self.__api_item_max)
        return tuple(Item.create_raw(item) for item in raw_items)
