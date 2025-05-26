from enum import Enum


class ItemType(Enum):
    NONE = 0
    ARMOR = 3


class ItemRarity(Enum):
    JUNK = 0
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5


class ItemEquipType(Enum):
    NONE = 0
    ARMOR = 2