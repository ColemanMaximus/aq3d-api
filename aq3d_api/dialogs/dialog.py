""" This module contains the the Dialog class."""

from collections.abc import Sequence

from aq3d_api import utils
from aq3d_api.dialogs.actor import DialogActor
from aq3d_api.dialogs.frame import DialogFrame


class Dialog:
    """
    The Dialog class groups together related dialog data such as
    individual dialog frames and actors.
    """

    def __init__(self,
                 id: int,
                 frames: Sequence[DialogFrame],
                 actors: Sequence[DialogActor]):
        """
        :param id: The ID of the dialog.
        :param frames: The frames which this dialog has.
        :param actors: The actors or NPCs which are within this dialog.
        """

        self.id = id
        self.frames = frames
        self.actors = actors

    @property
    def id(self) -> int:
        """
        Gets the id of the dialog.

        :return: Returns the dialog id.
        """

        return self.__id

    @id.setter
    def id(self, id: int):
        """
        Sets the id of the dialog.

        :param id: The id of the dialog.
        """

        if not isinstance(id, int):
            raise ValueError("Expected an integer for dialog id.")

        self.__id = id

    @property
    def frames(self) -> tuple[DialogFrame, ...]:
        """
        Gets all the frames within this dialog. Each frame being a collection
        of speaker, and text data.

        :return: The frames of this dialog.
        """

        return self.__frames

    @frames.setter
    def frames(self, frames: Sequence[DialogFrame]):
        """
        Sets all the frames this dialog has.

        :param frames: The frames for this dialog.
        """

        if not frames:
            return

        self.__frames = tuple(
            frame for frame in frames if isinstance(frame, DialogFrame)
        )

    @property
    def actors(self) -> tuple[DialogActor, ...]:
        """
        Gets all the dialog actor objects, which is essentially the NPCs
        within this dialog sequence.

        :return: The actors within this dialog.
        """

        return self.__actors

    @actors.setter
    def actors(self, actors: Sequence[DialogActor]):
        """
        Sets the actors (NPCs) who appear within this dialog sequence.

        :param actors: The actors within this dialog.
        """

        if not actors:
            return

        self.__actors = tuple(
            actor for actor in actors if isinstance(actor, DialogActor)
        )

    @classmethod
    def create_raw(cls, raw: dict):
        """
        Factory method to create a Dialog instance based on raw object given
        from the official AQ3D API.

        :param raw: The raw dialog object from the API.
        :return: The new created instance of a Dialog class.
        """

        if not isinstance(raw, dict):
            raise ValueError(
                "Expected a dict object for using the factory method."
            )

        frames = [DialogFrame.create_raw(raw_frame)
                  for raw_frame in raw.get("FrameCollection", [])]
        actors = [DialogActor.create_raw(raw_actor)
                  for raw_actor in raw.get("Characters", [])
                  if raw_actor.get("NPCID")]

        return cls(
            id = raw.get("ID"),
            frames = frames,
            actors = actors
        )

    def to_dict(self) -> dict:
        """
        Converts this class into a dict object.

        :return: Returns the dict representation of this object.
        """

        return utils.to_dict(self)

    def __str__(self) -> str:
        header = f"({self.id}) Dialog:"
        frames = ""
        for index, frame in enumerate(self.frames, 1):
            frames += f"\n  - (Frame {index}) {frame.speaker} > {frame.text}"

        return header + frames
