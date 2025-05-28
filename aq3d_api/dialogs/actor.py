""" This module contains the DialogActor class. """

from aq3d_api import utils


class DialogActor:
    """
    A DialogActor class is a representation of an NPC which appears within
    a dialog.
    """

    def __init__(self,
                 npc_id: int):
        """
        :param npc_id: The ID of the NPC.
        """

        self.npc_id = npc_id
    
    @property
    def npc_id(self) -> int:
        """
        Gets the NPC ID of the dialog actor.

        :return: The NPC ID of the actor.
        """

        return self.__npc_id
    
    @npc_id.setter
    def npc_id(self, npc_id: int):
        """
        Sets the NPC ID of the dialog actor.

        :param npc_id: The NPC ID of the actor.
        """

        if not isinstance(npc_id, int):
            raise ValueError("Expected an integer for dialog actors npc id.")

        self.__npc_id = npc_id

    def to_dict(self) -> dict:
        """
        Converts this object into a dict representation.

        :return: A dict representation of this object.
        """

        return utils.to_dict(self)

    @classmethod
    def create_raw(cls, raw: dict):
        """
        Factory method to create an instance of this class using raw dialog actor
        object from the official AQ3D API.

        :param raw: The raw object to use to create a DialogActor instance.
        :return: The new created instance of the DialogActor class.
        """

        if not isinstance(raw, dict):
            raise ValueError(
                "Expected a dict object for using the factory method."
            )

        npc_id = raw.get("NPCID")
        if npc_id:
            return cls(npc_id = npc_id)

        return None
