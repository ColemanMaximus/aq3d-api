""" This module contains the Map class. """
from aq3d_api import utils


class Map:
    """
    The class bundles together map data into
    a Map class.
    """

    def __init__(self,
                 id: int,
                 name: str,
                 description: str = "",
                 max_players: int = 1,
                 min_level: int = 1,
                 level_restriction: int = 0,
                 scaled: bool = False,
                 seasonal: bool = False,
                 dungeon: bool = False,
                 challenge: bool = False,
                 active: bool = False
                 ):
        """
        :param id: The ID of the map.
        :param name: Name of the map.
        :param description: The description for the map.
        :param max_players: How many players can be within this map.
        :param min_level: The minimum level recommended for this map.
        :param level_restriction: The level or higher required for this map.
        :param scaled: Does the map systems such as stats scale.
        :param seasonal: Is this map a seasonal map.
        :param dungeon: Is the map a dungeon.
        :param challenge: If the map contains a challenge.
        :param active: Whether the map is active, or instance joinable.
        """

        self.id = id
        self.name = name
        self.description = description
        self.max_players = max_players
        self.min_level = min_level
        self.level_restriction = level_restriction
        self.scaled = scaled
        self.seasonal = seasonal
        self.dungeon = dungeon
        self.challenge = challenge
        self.active = active

    @property
    def id(self) -> int:
        """
        Gets the id of the map.

        :return: Returns the map id.
        """

        return self.__id

    @id.setter
    def id(self, id: int):
        """
        Sets the id of the map.

        :param id: The id the map should have.
        """

        if not isinstance(id, int):
            raise ValueError("Expected a valid integer for map id.")

        self.__id = id

    @property
    def name(self) -> str:
        """
        Gets the name of the map.

        :return: Returns the maps name.
        """

        return self.__name

    @name.setter
    def name(self, name: str):
        """
        Sets the name of the map.

        :param name: The name which the map should have.
        """

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Expected a valid non empty string for the map name.")

        self.__name = name

    @property
    def description(self) -> str:
        """
        Gets the description of the map.

        :return: Returns the maps description.
        """

        return self.__description

    @description.setter
    def description(self, description: str):
        """
        Sets the description for the map.

        :param description: The description for the map.
        """

        if not isinstance(description, str):
            raise ValueError("Expected a string for the maps description.")

        self.__description = description

    @property
    def max_players(self) -> int:
        """
        Gets the amount of players allowed within this map.
        
        :return: The max players for the map.
        """

        return self.__max_players

    @max_players.setter
    def max_players(self, max_players: int):
        """
        Sets the maximum amount of players this map can have.
        
        :param max_players: The maximum players for this map.
        """
        
        if not isinstance(max_players, int) or max_players < 1:
            raise ValueError(
                "Expected a positive integer for the max players property setter."
            )

        self.__max_players = max_players

    @property
    def min_level(self) -> int:
        """
        Gets the minimum recommended level for the map.

        :return: The minimum recommended map level.
        """

        return self.__min_level

    @min_level.setter
    def min_level(self, min_level: int):
        """
        Sets the recommended minimum map level.

        :param min_level: The recommended minimum for the map.
        """

        if not isinstance(min_level, int) or min_level < 1:
            raise ValueError(
                "Expected a positive integer the minimum map level."
            )

        self.__min_level = min_level

    @property
    def level_restriction(self) -> int:
        """
        Gets the maps level restriction.

        :return: The level restriction for the map.
        """

        return self.__level_restriction

    @level_restriction.setter
    def level_restriction(self, level_restriction: int):
        """
        Sets the maps level restriction, which is the level they need
        to be to join.

        :param level_restriction: The level restriction for the map.
        """

        if not isinstance(level_restriction, int):
            raise ValueError(
                "Expected an integer for maps level restriction."
            )

        self.__level_restriction = level_restriction

    @property
    def scaled(self) -> bool:
        """
        Gets a bool whether the maps stats are scaled.

        :return: Returns the maps scaled factor.
        """

        return self.__scaled

    @scaled.setter
    def scaled(self, scaled: bool):
        """
        Sets the maps scaled factor, and if the maps stats are scaled.

        :param scaled: If the map stats are scaled.
        """

        if not isinstance(scaled, bool):
            raise ValueError("Expected a bool value for maps scaled factor.")

        self.__scaled = scaled

    @property
    def seasonal(self) -> bool:
        """
        Gets a bool whether the map is seasonal.

        :return: Returns if the map is seasonal.
        """

        return self.__seasonal

    @seasonal.setter
    def seasonal(self, seasonal: bool):
        """
        Sets if the map is seasonal.

        :param seasonal: If the map is seasonal.
        """

        if not isinstance(seasonal, bool):
            raise ValueError("Expected a bool value for map seasonal value.")

        self.__seasonal = seasonal

    @property
    def dungeon(self) -> bool:
        """
        Gets a bool whether the map is a dungeon.

        :return: Returns if the map is a dungeon.
        """

        return self.__dungeon

    @dungeon.setter
    def dungeon(self, dungeon: bool):
        """
        Sets if the map is a dungeon.

        :param dungeon: If the map is a dungeon.
        """

        if not isinstance(dungeon, bool):
            raise ValueError("Expected a bool value for map dungeon value.")

        self.__dungeon = dungeon

    @property
    def challenge(self) -> bool:
        """
        Gets a bool whether the map is a challenge.

        :return: Returns if the map is a challenge.
        """

        return self.__challenge

    @challenge.setter
    def challenge(self, challenge: bool):
        """
        Sets if the map is a challenge.

        :param challenge: If the map is a challenge.
        """

        if not isinstance(challenge, bool):
            raise ValueError("Expected a bool value for map challenge value.")

        self.__challenge = challenge

    @property
    def active(self) -> bool:
        """
        Gets a bool whether the map is active and joinable.

        :return: Returns if the map is active.
        """

        return self.__active

    @active.setter
    def active(self, active: bool):
        """
        Sets if the map is active and joinable.

        :param active: If the map is active.
        """

        if not isinstance(active, bool):
            raise ValueError("Expected a bool value for map active value.")

        self.__active = active

    @classmethod
    def create_raw(cls, raw: dict):
        """
        Factory method to create a Map instance from raw
        data directly from the official API.

        :param raw: The raw JSON data from the API.
        :return: Map instance using the raw data.
        """

        if not isinstance(raw, dict) or not raw:
            raise ValueError("Expected a valid raw dict object of map data.")

        map = raw["map"]
        return cls(
            id = map.get("ID"),
            name = map.get("DisplayName"),
            description = map.get("Description", ""),
            max_players = map.get("MaxUsers", 1),
            min_level = map.get("MinLevel", 1),
            level_restriction = map.get("levelRestriction", 0),
            scaled = map.get("IsScaled", False),
            seasonal = map.get("IsSeasonal", False),
            dungeon = map.get("IsDungeon", False),
            challenge = map.get("IsChallenge", False),
            active = map.get("bActive", False)
        )

    def to_dict(self):
        return utils.to_dict(self)

    def __str__(self) -> str:
        return str(self.to_dict())
