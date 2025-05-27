""" This module contains the ItemAttributes class. """


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
