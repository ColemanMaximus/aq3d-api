""" This module contains the Enum class for item types. """

from enum import Enum


class ItemType(Enum):
    """ The Enum class for item types. """

    ITEM = 0
    QUEST_ITEM = 1
    CLASS = 2
    ARMOR = 3
    ROBE = 4
    BELT = 5
    BRACERS = 6
    GLOVES = 7
    BOOTS = 8
    SHOULDERS = 9
    BACK = 10
    HELM = 11
    SWORD = 12
    CONSUMABLE = 13
    CHEST = 14
    TOKEN = 15
    CLASS_TOKEN = 16
    PISTOL = 17
    PET = 18
    CRYSTAL = 19
    FISHING_ROD = 20
    PICKAXE = 21
    BOW = 22
    FISH = 23
    ORE = 24
    BOBBER = 25
    HOUSE_ITEM = 26
    MAP = 27
    MOMENT = 28
    MOUNT = 29
    TRAVEL_FORM = 30
    BACK_ACCESSORY = 31
    HEROIC_SKILL = 32
