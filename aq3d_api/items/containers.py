""" This module contains the Items class container. """
from collections.abc import Generator
from pathlib import Path

import aq3d_api.utils as utils
from aq3d_api.items.item import Item
from aq3d_api.enums.item_type import ItemType
from aq3d_api.enums.item_equip_type import ItemEquipType
from aq3d_api.enums.item_rarity import ItemRarity
from aq3d_api.api.updater import APIUpdater
from aq3d_api.api.handler import send_req_items


class Items(APIUpdater):
    """
    Items container class to bundle items together.
    Supports the APIUpdater class.
    """

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

    @property
    def items(self) -> Generator:
        """
        Returns a generator of Item objects within the Items container class.

        :return: Returns a generator of Item objects.
        """

        return (item for item in self.__items)

    @items.setter
    def items(self, items):
        """
        Sets the items container to a list of Item objects.

        :param items: The items to supply the container.
        """

        self.__items = items

    def items_by_type(self, filter_type: ItemType | ItemEquipType | ItemRarity) -> Generator[Item]:
        """
        Returns a filtered list of items by enum types.

        Accepts an ItemType, ItemEquipType or ItemRarity types.

        :param filter_type: The enum type to filter by.
        :return: Generator of filtered items.
        """

        if isinstance(filter_type, ItemRarity):
            return (item for item in self.items if item.rarity == filter_type)
        if isinstance(filter_type, ItemEquipType):
            return (item for item in self.items if item.equip_type == filter_type)

        return (item for item in self.items if item.type == filter_type)

    def items_by_keypair(self, key: str, value) -> Generator[Item]:
        """
        Returns a filtered list of Item objects if they have
        the matching key value pair.

        :param key: The key you want to filter by.
        :param value: The value the key should be to be considered a match.
        :return: A generator of filtered Item objects.
        """

        if not isinstance(key, str):
            raise ValueError("Expected a string of an items key.")

        if not value:
            raise ValueError("Expected a non empty value for keys value.")

        return (item for item in self.items if item.__getattribute__(key))

    def to_csv(self, path: Path):
        """
        Useful method to export all the items within this Items object
        into a csv file.

        :param path: The path to write the items to.
        """

        if not isinstance(path, Path):
            raise ValueError("Expected a Path instance to write the items to.")

        utils.to_csv(list(self.items), path)

    def __fetch_fromapi(self) -> list | None:
        """
        Requests items to be fetched from the official API.

        :return: The fetched items as a list of Item objects.
        """

        raw_items = send_req_items(self.api_item_min, self.api_item_max)
        items = [Item.create_raw(item) for item in raw_items]

        return items

    def __str__(self) -> str:
        string = f"Items ({len(self.__items)}):"
        for item in self.items:
            string += f"\n  - ({item.id} | {item.type.name}) {item.name}"

        return string

    def __iter__(self) -> Generator[Item]:
        return self.items
