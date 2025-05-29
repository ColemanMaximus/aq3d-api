"""
This module defines the Dialog class, which encapsulates dialog data such
as dialog frames and actors (NPCs) for AQ3D dialogs.
"""

from collections.abc import Sequence

from aq3d_api import utils
from aq3d_api.dialogs.actor import DialogActor
from aq3d_api.dialogs.frame import DialogFrame


class Dialog:
    """
    Represents a dialog sequence in AQ3D, containing dialog frames
    and actors (NPCs).
    """

    def __init__(self, **data):
        """
        ### Parameters:
            **id (int)**: The id of the dialog.
            **frames (list[DialogFrame])**: A list of dialog frames belonging to this dialog.
            **actors (list[DialogActor])**: The dialog actors (NPCs) which are in this dialog.

        ### Example
        ```
        {
            "id": 1
            "frames": [DialogFrame, DialogFrame],
            "actors": [DialogActor]
        }
        ```
        """

        self.id = data["id"]
        self.frames = data["frames"]
        self.actors = data["actors"]

    @property
    def id(self) -> int:
        """
        Returns the unique id associated with this dialog instance.

        ### Returns:
            **int**: The unique ID of the dialog.
        """

        return self.__id

    @id.setter
    def id(self, id: int):
        """
        Sets the dialog ID.

        ### Parameters:
            **id (int)**: The unique id for the dialog.

        ### Raises:
            **ValueError**: If the provided id is not an integer.
        """

        if not isinstance(id, int):
            raise ValueError("Expected an integer for dialog id.")

        self.__id = id

    @property
    def frames(self) -> tuple[DialogFrame, ...]:
        """
        Returns a tuple containing all dialog frames associated with this dialog.

        ### Returns:
            **tuple[DialogFrame]**: DialogFrame objects representing the frames of the dialog.
        """

        return self.__frames

    @frames.setter
    def frames(self, frames: Sequence[DialogFrame]):
        """
        Sets the dialog frames for this dialog.

        ### Parameters:
            **frames (Sequence[DialogFrame])**: A sequence of DialogFrame objects to be set for the dialog.

        ### Notes:
            - Only instances of DialogFrame are retained; other types are ignored.
            - If the provided sequence is empty or None, no changes are made.
        """

        if not frames:
            return

        self.__frames = tuple(
            frame for frame in frames if isinstance(frame, DialogFrame)
        )

    @property
    def actors(self) -> tuple[DialogActor, ...]:
        """
        Returns a tuple containing all dialog actors associated
        with this dialog.

        ### Returns:
            **tuple[DialogActor]**: DialogActor objects of the dialog.
        """

        return self.__actors

    @actors.setter
    def actors(self, actors: Sequence[DialogActor]):
        """
        Sets the dialog actors for this dialog.

        ### Parameters:
            **actors (Sequence[DialogActor])**: A sequence of DialogActor objects to be set for the dialog.

        ### Notes:
            - Only instances of DialogActor are retained; other types are ignored.
            - If the provided sequence is empty or None, no changes are made.
        """

        if not actors:
            return

        self.__actors = tuple(
            actor for actor in actors if isinstance(actor, DialogActor)
        )

    @classmethod
    def create_raw(cls, raw: dict):
        """
        Factory method to create an instance of the class from a raw dictionary.

        ### Parameters:
            **raw (dict)**: A dictionary containing dialog data. Expected keys include
                - **ID (int)**: The dialog identifier.
                - **FrameCollection (list)**: A list of frame dictionaries to be converted into DialogFrame instances.
                - **Characters (list)**: A list of character dictionaries to be converted into DialogActor instances.

        ### Returns:
            **Dialog**: An instance of the class initialized with the provided data.

        ### Raises:
            **ValueError**: If the provided raw argument is not a dictionary.
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
            id = raw.get("ID", -1),
            frames = frames,
            actors = actors
        )

    def to_dict(self) -> dict:
        """
        Converts the current instance into a dictionary representation.

        ### Returns:
            **dict**: A dictionary containing all the attributes of the instance.
        """

        return utils.to_dict(self)

    def __str__(self) -> str:
        header = f"({self.id}) Dialog:"
        frames = ""
        for index, frame in enumerate(self.frames, 1):
            frames += f"\n  - (Frame {index}) {frame.speaker} > {frame.text}"

        return header + frames
