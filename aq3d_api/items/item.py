""" This module contains the Item class. """

import aq3d_api.utils as utils

from aq3d_api.items.attributes import ItemAttributes
from aq3d_api.enums.item_type import ItemType
from aq3d_api.enums.item_equip_type import ItemEquipType
from aq3d_api.enums.item_rarity import ItemRarity

class Item(ItemAttributes):
    """ The Item class defines an item object. """

    def __init__(self,
                 item_id: int,
                 name: str,
                 level: int = 1,
                 description: str = "",
                 price: int = 0,
                 item_type: ItemType = ItemType.ITEM,
                 equip_type: ItemEquipType = ItemEquipType.NONE,
                 rarity: ItemRarity = ItemRarity.JUNK,
                 stack_size: int = 1,
                 version: int = 1,
                 health: float = 0,
                 attack: float = 0,
                 armor: float = 0,
                 evasion: float = 0,
                 critical: float = 0,
                 is_cosmetic: bool = False,
                 is_dc_purchasable: bool = False
                 ):

        """

        :param item_id: ID of the item.
        :param name: Name of the item.
        :param level: Level of the item.
        :param description: Description of the item.
        :param price: How much the item costs.
        :param item_type: What kind of type is the item.
        :param equip_type: Which equip slot does the item fit into.
        :param rarity: The rarity of the item.
        :param stack_size: How many of this item can be held in a stack.
        :param version: The versioning number for this item.
        :param health: How much health this item gives.
        :param attack: The attack of the item.
        :param armor: The armor the item gives.
        :param evasion: How much evasion the item gives.
        :param critical: How much critical damage the item does.
        :param is_cosmetic: If the item contains item attributes or not.
        :param is_dc_purchasable: If the item can be purchased using Dragon Crystals.
        """

        self.id = item_id
        self.name = name
        self.level = level
        self.description = description
        self.price = price
        self.type = item_type
        self.equip_type = equip_type
        self.rarity = rarity
        self.stack_size = stack_size
        self.version = version
        self.cosmetic = is_cosmetic
        self.dc_purchasable = is_dc_purchasable
        super().__init__(health, attack, armor, evasion, critical)

    @property
    def id(self) -> int:
        """
        Returns the id of the item.

        :return: Returns the item id.
        """

        return self.__id

    @id.setter
    def id(self, sid: int):
        """
        Sets the id of the item.

        :param sid: ID the item should have.
        """

        if not isinstance(sid, int):
            raise ValueError("Expected an integer for item id.")

        self.__id = sid

    @property
    def name(self) -> str:
        """
        Returns the name of the item.

        :return: Name of the item.
        """

        return self.__name

    @name.setter
    def name(self, name: str):
        """
        Sets the name of the item to a non-empty value.

        :param name: The name the item should have.
        """

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Expected a valid non-empty string for the items name.")

        self.__name = name

    @property
    def description(self) -> str:
        """
        Returns the description of the item.

        :return: The description of the item.
        """

        return self.__description

    @description.setter
    def description(self, description: str):
        """
        Sets the description of the item.

        :param description: Description the item should have.
        """

        if not isinstance(description, str):
            raise ValueError("Expected a string for the description of an item.")

        self.__description = description

    @property
    def price(self) -> int:
        """
        Returns the price or cost of the item.

        :return: The price of the item.
        """

        return self.__price

    @price.setter
    def price(self, value: int):
        """
        Sets the price of the item.

        :param value: The price the item should cost.
        """

        if not isinstance(value, int):
            raise ValueError("Expected an integer value for the items price.")

        self.__price = value

    @property
    def type(self) -> ItemType:
        """
        Returns the type of the item as a ItemType Enum type.

        :return: Type of the item.
        """

        return self.__type

    @type.setter
    def type(self, item_type: ItemType):
        """
        Sets the type of the item to an ItemType Enum type.

        :param item_type: The type which the item should be.
        """

        if not isinstance(item_type, ItemType):
            raise ValueError("Expected a type from the ItemType Enum class.")

        self.__type = item_type

    @property
    def equip_type(self) -> ItemEquipType:
        """
        Returns the equip type of the item as an ItemEquipType Enum class type.

        :return: Equip type of the item.
        """

        return self.__equip_type

    @equip_type.setter
    def equip_type(self, equip_type: ItemEquipType):
        """
        Sets the equip type of the item to a type of the ItemEquipType Enum class.

        :param equip_type: The equip type the item should have.
        """

        if not isinstance(equip_type, ItemEquipType):
            raise ValueError(
                "Expected an ItemEquipType Enum type for the equip type of the item."
            )

        self.__equip_type = equip_type

    @property
    def rarity(self) -> ItemRarity:
        """
        Returns the rarity of the item as an ItemRarity Enum type.

        :return: The rarity of the item.
        """

        return self.__rarity

    @rarity.setter
    def rarity(self, rarity: ItemRarity):
        """
        Sets the rarity of the item to an ItemRarity Enum class type.

        :param rarity: The rarity type the item should have.
        """

        if not isinstance(rarity, ItemRarity):
            raise ValueError("Expected an ItemRarity enum type for the items rarity.")

        self.__rarity = rarity

    @property
    def stack_size(self) -> int:
        """
        Returns the size in which the item stacks.

        :return: The items stack size.
        """

        return self.__stack_size

    @stack_size.setter
    def stack_size(self, size: int):
        """
        Sets the size in which the item stacks.

        :param size: How many items are in a stack.
        """

        if not isinstance(size, int):
            raise ValueError("Expected an integer above 0 for stack size.")

        self.__stack_size = size

    @property
    def version(self) -> int:
        """
        Returns the version of the item, which is defined by how many times
        the asset bundle has been updated.

        :return: The version of the item.
        """

        return self.__version

    @version.setter
    def version(self, version: int):
        """
        Sets the items versioning number.

        :param version: The version the item should have.
        """

        if not isinstance(version, int):
            raise ValueError("Expected an integer for an items version.")

        self.__version = version

    @property
    def cosmetic(self) -> bool:
        """
        Returns a bool if the item is of a cosmetic nature.

        :return: Bool based on if the item is cosmetic.
        """

        return self.__cosmetic

    @cosmetic.setter
    def cosmetic(self, value: bool):
        """
        Sets the cosmetic nature of the item.

        :param value: A bool based on if the item is cosmetic.
        """

        if not isinstance(value, bool):
            raise ValueError("Expected a bool value for the cosmetic property setter.")

        self.__cosmetic = value

    @property
    def dc_purchasable(self) -> bool:
        """
        Returns a bool if the item can be bought using Dragon Crystals, whether
        in crafting speedups or in a shop.

        :return: If the item can be bought using Dragon Crystals.
        """

        return self.__dc_purchasable

    @dc_purchasable.setter
    def dc_purchasable(self, value: bool):
        """
        Sets the bool value whether the item can be purchased
        using Dragon Crystals.

        :param value: Can the item be purchased with Dragon Crystals.
        """

        if not isinstance(value, bool):
            raise ValueError("Expected a bool value for if the item is DC purchasable.")

        self.__dc_purchasable = value

    @classmethod
    def create_raw(cls, raw):
        """
        Factory method to create an Item object by giving raw json
        data inputted directly from the official AQ3D API.

        :param raw: The originally structured json data from the API.
        :return: Returns a new instance of the Item class.
        """

        return cls(
            item_id=raw.get("ID"),
            name=raw.get("Name"),
            level=raw.get("Level", 1),
            description=raw.get("Desc", ""),
            price=raw.get("Cost", 0),
            item_type=utils.to_enum(
                ItemType, raw.get("Type", 0), ItemType.ITEM
            ),
            equip_type=utils.to_enum(
                ItemEquipType, raw.get("EquipSlot", 0), ItemEquipType.NONE
            ),
            rarity=utils.to_enum(
                ItemRarity, raw.get("Rarity", 0), ItemRarity.JUNK
            ),
            stack_size=raw.get("MaxStack", 1),
            version=raw.get("bundle")["Version"] if "bundle" in raw else 1,
            health=raw.get("MaxHealth", 0),
            attack=raw.get("Attack", 0),
            armor=raw.get("Armor", 0),
            evasion=raw.get("Evasion", 0),
            critical=raw.get("Crit", 0),
            is_cosmetic=raw.get("IsCosmetic", False),
            is_dc_purchasable=raw.get("IsMC", False)
        )

    def to_dict(self) -> dict:
        """
        Quickly converts the objects attributes to a dict.

        :return: The dict representation of the objects attributes.
        """

        return utils.to_dict(self)

    def __str__(self) -> str:
        return str(self.to_dict())
