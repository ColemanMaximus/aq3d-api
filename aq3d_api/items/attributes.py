""" This module contains the ItemAttributes class. """

class ItemAttributes:
    """
    A class for item attributes, including stats such as
    health, attack, armor, evasion and critical.
    """

    def __init__(self, **data):
        """
        :param health: Health the item gives.
        :param attack: Attack the item gives.
        :param armor: Armor the item gives.
        :param evasion: Health the item gives.
        :param critical: Critical damage the item gives.
        """

        self.health = data["health"]
        self.attack = data["attack"]
        self.armor = data["armor"]
        self.evasion = data["evasion"]
        self.critical = data["critical"]
