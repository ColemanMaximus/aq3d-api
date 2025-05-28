""" This module contains the Enum class for item equip types. """

from enum import Enum


class ItemEquipType(Enum):
    """ The Enum class for item equip types. """

    NONE = 0
    CLASS = 1
    ARMOR = 2
    BELT = 3
    BRACERS = 4
    GLOVES = 5
    BOOTS = 6
    SHOULDERS = 7
    BACK = 8
    HELM = 9
    WEAPON = 10
    PISTOL = 11
    PET = 12
    BOW = 13
    FISHING_ROD = 14
    PICKAXE = 15
    BOBBER = 16
    BACK_ACCESSORY = 17
    NPC_EQUIP = 18
