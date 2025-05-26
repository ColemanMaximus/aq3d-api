"""
This module handles working with Item objects
and some useful methods to operate on them.
"""

import aq3d_api.utils as utils
from aq3d_api.enums import ItemType, ItemRarity, ItemEquipType


class ItemAttributes:
    """
    A class for item attributes, including stats such as
    health, attack, armor, evasion and critical.
    """

    def __init__(self,
                 health: float = 0,
                 attack: float = 0,
                 armor: float = 0,
                 evasion: float = 0,
                 critical: float = 0):

        """

        :param health: Health the item gives.
        :param attack: Attack the item gives.
        :param armor: Armor the item gives.
        :param evasion: Health the item gives.
        :param critical: Critical damage the item gives.
        """

        self.health = health
        self.attack = attack
        self.armor = armor
        self.evasion = evasion
        self.critical = critical


class Item(ItemAttributes):
    """ The Item class defines an item object. """

    def __init__(self,
                 item_id: int,
                 name: str,
                 level: int = 1,
                 description: str = "",
                 price: int = 0,
                 item_type: ItemType = ItemType.NONE,
                 equip_type: ItemEquipType = ItemEquipType.NONE,
                 rarity: ItemRarity = ItemRarity.JUNK,
                 stack_size: int = 1,
                 version: int = 1,
                 health: float = 0,
                 attack: float = 0,
                 armor: float = 0,
                 evasion: float = 0,
                 critical: float = 0,
                 is_cosmetic: bool = False
                ):

        """

        :param item_id: ID of the item.
        :param name: Name of the item.
        :param level: Level of the item.
        :param description: Description of the item.
        :param price: How much the item costs.
        :param item_type: What kind of type is the item.
        :param equip_type: Where does the item equip to.
        :param rarity: The rarity of the item.
        :param stack_size: How many of this item can be held in a stack.
        :param version: The versioning number for this item.
        :param health: How much health this item gives.
        :param attack: The attack of the item.
        :param armor: The armor the item gives.
        :param evasion: How much evasion the item gives.
        :param critical: How much critical damage the item does.
        :param is_cosmetic: If the item contains item attributes or not.
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
        super().__init__(health, attack, armor, evasion, critical)

    @property
    def cosmetic(self) -> bool:
        """
        Returns a bool if the item is of a cosmetic nature.

        :return: Returns a bool based on if the item is cosmetic.
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

    @classmethod
    def create_raw(cls, raw):
        """
        Factory method to create an Item object by giving raw json
        data inputted directly from the official AQ3D API.

        :param raw: The originally structured json data from the API.
        :return: Returns a new instance of the Item class.
        """

        return cls(
            item_id = raw.get("ID"),
            name = raw.get("Name"),
            description = raw.get("Desc", ""),
            price = raw.get("Cost", 0),
            item_type = utils.to_enum(
                ItemType, raw.get("Type", 0), ItemType.NONE
            ),
            equip_type = utils.to_enum(
                ItemEquipType, raw.get("EquipSlot", 0), ItemEquipType.NONE
            ),
            rarity = utils.to_enum(
                ItemRarity, raw.get("Rarity", 0), ItemRarity.JUNK
            ),
            stack_size = raw.get("MaxStack", 1),
            health = raw.get("MaxHealth", 0),
            attack = raw.get("Attack", 0),
            armor = raw.get("Armor", 0),
            evasion = raw.get("Evasion", 0),
            critical = raw.get("Crit", 0),
            is_cosmetic = raw.get("IsCosmetic", False)
        )

    def __str__(self) -> str:
        # Filter any redundant keypair values from the object dict.
        filtered_dict = {
            key.split("__")[-1]: value
            for key, value in self.__dict__.items() if value
        }

        return str(filtered_dict)
