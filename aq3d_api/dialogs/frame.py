""" This module contains the DialogFrame class. """

from aq3d_api import utils


class DialogFrame:
    """
    A DialogFrame class is a representation of frame within a dialog,
    containing the speaker, title of the speaker, and the text.
    """

    def __init__(self, **data):
        """
        :param speaker: The speaker of the dialog frame.
        :param title: The title of the speaker.
        :param text: The text within this dialog frame.
        """

        self.speaker = data["speaker"]
        self.title = data["title"]
        self.text = data["text"]

    @property
    def speaker(self) -> str:
        """
        Gets the speaker in this dialog frame.

        :return: Returns the dialog frame speaker.
        """

        return self.__speaker

    @speaker.setter
    def speaker(self, speaker: str):
        """
        Sets the dialog frame speaker.

        :param speaker: The speaker for this dialog frame.
        """

        if not isinstance(speaker, str):
            raise ValueError(
                "Expected a string for the dialog frame speakers name."
            )

        self.__speaker = speaker

    @property
    def title(self) -> str:
        """
        Gets the title of the speaker in this dialog frame.

        :return: The title of the speaker for this dialog frame.
        """

        return self.__title

    @title.setter
    def title(self, title: str):
        """
        Sets the speakers title within the dialog frame.

        :param title: The title the speaker should have.
        """

        if not isinstance(title, str):
            raise ValueError(
                "Expected a string for the dialog frame speakers title."
            )

        self.__title = title

    @property
    def text(self) -> str:
        """
        Gets the dialog frames text.

        :return: Returns the dialog frames text.
        """

        return self.__text

    @text.setter
    def text(self, text: str):
        """
        Sets the text within this dialog frame

        :param text: The text to use within this dialog frame.
        """

        if not isinstance(text, str):
            raise ValueError("Expected a string for the dialog frames text.")

        self.__text = text

    def to_dict(self) -> dict:
        """
        Converts this object into a dict representation.

        :return: A dict representation of this object.
        """

        return utils.to_dict(self)

    @classmethod
    def create_raw(cls, raw: dict):
        """
        Factory method to create an instance of this class using raw dialog frame
        object from the official AQ3D API.

        :param raw: The raw object to use to create a DialogFrame instance.
        :return: The new created instance of the DialogFrame class.
        """

        if not isinstance(raw, dict):
            raise ValueError(
                "Expected a dict object for using the factory method."
            )

        return cls(
            speaker = raw.get("DialogueName", ""),
            title = raw.get("DialogueTitle", ""),
            text = raw.get("DialogueText", "")
        )
