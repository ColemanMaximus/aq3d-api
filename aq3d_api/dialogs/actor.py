"""
This module defines the DialogActor class, which represents an NPC actor
within a dialog in the AQ3D API.
"""

from aq3d_api import utils


class DialogActor:
    """
    Represents a dialog actor (NPC) in the AQ3D API.
    """

    def __init__(self, npc_id: int):
        """
        ### Parameters:
            **npc_id (int)**: The unique id of the NPC associated with this actor.
        """

        self.npc_id = npc_id

    @property
    def npc_id(self) -> int:
        """
        Returns the unique id of the NPC associated with this actor.

        ### Returns:
            **int**: The NPC's unique identifier.
        """

        return self.__npc_id

    @npc_id.setter
    def npc_id(self, npc_id: int):
        """
        Sets the NPC (Non-Player Character) ID for the dialog actor.

        ### Parameters:
            **npc_id (int)**: The unique id of the NPC.

        ### Raises:
            **ValueError**: If npc id is not an integer.
        """

        if not isinstance(npc_id, int):
            raise ValueError("Expected an integer for dialog actors npc id.")

        self.__npc_id = npc_id

    def to_dict(self) -> dict:
        """
        Converts the current instance into a dictionary representation.

        ### Returns:
            **dict**: A dictionary containing all the attributes of the instance.
        """

        return utils.to_dict(self)

    @classmethod
    def create_raw(cls, raw: dict):
        """
        Factory method to create an instance of the class from a raw dictionary.

        ### Parameters:
            **raw (dict)**: A dictionary containing the data to initialize the instance.

        ### Returns:
            DialogActor: New instance of the DialogActor.

        ### Raises:
            **ValueError**: If the provided raw argument is not a dictionary.
        """

        if not isinstance(raw, dict):
            raise ValueError(
                "Expected a dict object for using the factory method."
            )

        return cls(raw.get("NPCID", -1))
