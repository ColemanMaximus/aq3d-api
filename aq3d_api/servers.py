""" This module contains classes and functions for capturing server metadata."""

class Server:
    """ Metadata about a server is bundled up in this Server class. """

    def __init__(self, id: int, name: str):
        """
        :param id: ID of the server.
        :param name: The servers name.
        """

        self.id = id
        self.name = name
        self.players = 0
        self.max_players = 0

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        if not id or not isinstance(id, int):
            raise ValueError("Invalid id for the server was provided.")

        self.__id = id

    @property
    def name(self) -> str:
        """
        Returns the name of the server.

        :return str: The name of the server.
        """

        return self.__name

    @name.setter
    def name(self, name: str):
        """
        Sets the name of the server.

        Server names can't be an empty value, they require a valid non-empty string.

        :param name: The name the server should have.
        """

        if not isinstance(name, str) or not name.strip():
            raise ValueError("None/invalid name was provided for the server.")

        self.__name = name

    @property
    def players(self) -> int:
        """
        Returns the number of online players.

        :return int: Number of online players.
        """

        return self.__players

    @players.setter
    def players(self, value: int):
        """
        Sets the number of players online to the value.

        :param value: The number of players online.
        """

        if not isinstance(value, int):
            raise ValueError("Expected an integer value.")

        self.__players = value

    @property
    def max_players(self) -> int:
        """
        Returns the maximum amount of players allowed on the server at once.

        :return int: Returns the maximum amount of players.
        """

        return self.__max_players

    @max_players.setter
    def max_players(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Invalid max players value provided. Expected an integer, or a positive number.")

        self.__max_players = value

    @property
    def is_full(self) -> bool:
        """
        Returns a bool depending on if the server has reached or exceeded its player limit.

        :return bool: Returns bool based on player limits.
        """

        return self.players >= self.max_players