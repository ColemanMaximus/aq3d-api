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
from aq3d_api.api.service import APIService
from aq3d_api.api.handlers.types import Handlers


class Items(DataContainer, APIService):
    """
    A container class for managing and filtering collections of Item objects,
    with optional support for fetching and auto-updating items from an external API.
    """

    def __init__(self, options: dict = {}):
        """
        ### Parameters:
            **auto-update (bool)**: Whether to automatically update items from the API.
            **min-index (int)**: Minimum number of items by ID range.
            **max-index (int)**: Maximum number of items by ID range.
            **update-interval (int)**: Interval (in seconds) for automatic updates.

        ### Example
        ```
        {
            "auto-update": True,
            "min-index": 1,
            "max-index": 10,
            "update-interval": 1000
        }
        ```
        """

        DataContainer.__init__(self)
        APIService.__init__(self, options)

    @property
    def items(self) -> list[Item]:
        """
        Returns each Item object contained in the container.


        ### Returns:
            **list[Item]**: Items from the container.
        """

        self.update()
        return list(self._objs)

    def by_type(self,
                      filter_type: ItemType
                                   | ItemEquipType
                                   | ItemRarity
                       ) -> Generator[Item]:
        """
        Yields items from the container that match the specified filter type.

        Depending on the type of `filter_type`, this method filters items by their rarity,
        equipment type, or item type.

        ### Parameters:
            **filter_type (ItemType | ItemEquipType | ItemRarity)**: The item type to filter by.

        ### Yields:
            **Generator[Item]**: Items from the container that match the specified filter type
        """

        if isinstance(filter_type, ItemRarity):
            return (item for item in self.items if item.rarity == filter_type)
        if isinstance(filter_type, ItemEquipType):
            return (item for item in self.items if item.equip_type == filter_type)

        return (item for item in self.items if item.type == filter_type)

    def by_keypair(self, key: str, value) -> Generator[Item]:
        """
        Yields items from the container whose attribute `key` matches the specified `value`.

        ### Parameters:
            **key (str)**: The name of the attribute to filter items by.
            **value (Any)**: The value that the item's attribute should match.

        ### Raises:
            **ValueError**: If `key` is not a string.
            **ValueError**: If `value` is empty or None.


        ### Yields:
            **Generator[Item]**: Items whose attribute `key` equals `value`.
        """

        if not isinstance(key, str):
            raise ValueError("Expected a string of an items key.")

        if not value:
            raise ValueError("Expected a non empty value for keys value.")

        return (item for item in self.items if item.__getattribute__(key))

    def _fetch(self) -> tuple:
        """
        Fetches item data from the API within the specified item ID range
        and returns a tuple of Item objects.
        """

        return tuple([self, Handlers.ITEMS, Item]) # type: ignore

    def __getitem__(self, index: int) -> Item:
        return self.items[index]

    def __iter__(self) -> Generator:
        return (item for item in self.items)
