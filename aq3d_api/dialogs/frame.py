"""
This module defines the DialogFrame class, which represents a single frame
within a dialog in the AQ3D API context.
"""

from aq3d_api import utils


class DialogFrame:
    """
    A DialogFrame encapsulates information about the speaker,
    their title, and the dialog text.
    """

    def __init__(self, **data):
        """
        ### Parameters:
            **speaker (str)**: The speaker of the text.
            **title (str)**: The title of the speaker.
            **text (str)**: The text which is spoken by the speaker.

        ### Example
        ```
        {
            "speaker": "John"
            "title": "The Bold",
            "text": "Welcome to this land."
        }
        ```
        """

        self.speaker = data["speaker"]
        self.title = data["title"]
        self.text = data["text"]

    @property
    def speaker(self) -> str:
        """
        Returns the name of the current speaker.

        ### Returns:
            **str**: The name of the speaker.
        """

        return self.__speaker

    @speaker.setter
    def speaker(self, speaker: str):
        """
        Sets the name of the speaker for the dialog frame.

        ### Parameters:
            **speaker (str)**: The name of the speaker.

        ### Raises:
            **ValueError**: If the provided speaker is not a string.

        """

        if not isinstance(speaker, str):
            raise ValueError(
                "Expected a string for the dialog frame speakers name."
            )

        self.__speaker = speaker

    @property
    def title(self) -> str:
        """
        Gets the title of the dialog speaker.

        ### Returns:
            **str**: The title of the dialog speaker.

        """

        return self.__title

    @title.setter
    def title(self, title: str):
        """
        Sets the title of the dialog speaker.

        ### Parameters:
            **title (str)**: The title to set for the dialog speaker.

        ### Raises:
            **ValueError**: If the provided title is not a string.
        """

        if not isinstance(title, str):
            raise ValueError(
                "Expected a string for the dialog frame speakers title."
            )

        self.__title = title

    @property
    def text(self) -> str:
        """
        Returns the text content of the dialog frame.

        ### Returns:
            **str**: The text associated with this dialog frame.
        """

        return self.__text

    @text.setter
    def text(self, text: str):
        """
        Sets the text for the dialog frame.

        ### Parameters:
            **text (str)**: The text to display in the dialog frame.

        ### Raises:
            **ValueError**: If the provided text is not a string.
        """

        if not isinstance(text, str):
            raise ValueError("Expected a string for the dialog frames text.")

        self.__text = text

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
            **raw (dict)**: A dictionary containing dialogue data with possible keys:
                - **DialogueName**: The name of the speaker.
                - **DialogueTitle**: The title of the speaker.
                - **DialogueText**: The main text of the dialogue.

        ### Returns:
            **DialogFrame**: An instance of the class initialized with the
            provided dialogue data.

        ### Raises:
            **ValueError**: If the provided raw argument is not a dictionary.
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
