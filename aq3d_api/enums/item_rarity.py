""" This module contains the Enum class for item rarity types. """

from enum import Enum


class ItemRarity(Enum):
    """ The Enum class for item rarity types. """

    JUNK = 0
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5
