"""
This module defines the DataContainer class, which provides a generic container
for storing and processing collections of objects, with utility methods for
exporting the contained data to CSV and JSON formats.
"""

from collections.abc import Generator
from pathlib import Path

from aq3d_api import utils


class DataContainer:
    """
    A generic container class for managing and exporting collections of objects.

    Provides methods for adding objects, iterating, and exporting
    the collection to CSV and JSON files.
    """

    def __init__(self):
        self.__objs = []

    @property
    def _objs(self) -> Generator:
        """
        Returns a generator that yields all objects stored in the container.

        ### Yields:
            **Generator (obj)**: Each object contained within the container.
        """

        return (obj for obj in self.__objs)

    @_objs.setter
    def _objs(self, objs):
        """
        Sets the internal list of objects for the container.

        ### Parameters:
            **objs (Iterable)**: The collection of objects to be stored in the container.
        """

        self.__objs = objs

    def append(self, cls: type, overwrite = False, *objs):
        """
        Appends objects to the container if they are an instance
        of the specified class.

        ### Parameters:
            **cls (type)**: The class or type that `objs` are expected to be an instance of.
            **objs (Any)**: The objects to be appended to the container.
            **overwrite (bool)**: Overwrites all objects inside the container
            with new objects.
        """

        if overwrite:
            self.__objs = [obj for obj in objs[0] if isinstance(obj, cls)]
            return

        # *objs returns a tuple with the list of items inside
        # so we have to unpack the tuple first.
        for obj in objs[0]:
            if not isinstance(obj, cls):
                continue

            self.__objs.append(obj)

    def to_csv(self, path: Path):
        """
        Export the objects contained in this container to a CSV file.

        This method serializes the objects stored in the container
        and writes them to the specified CSV file.

        ### Parameters:
            **path (Path)**: The file path where the CSV will be saved.

        ### Raises:
            **ValueError**: If the provided path is not an instance of pathlib.Path.
        """

        if not isinstance(path, Path):
            raise ValueError("Expected a Path instance to write the objects to.")

        utils.to_csv(list(self._objs), path)

    def to_json_file(self, path: Path):
        """
        Serializes the container's objects to a JSON file at the specified path.

        ### Parameters:
            **path (Path)**: The file system path where the JSON file will be written.

        ### Raises:
            **ValueError**: If the provided path is not an instance of pathlib.Path.
        """

        if not isinstance(path, Path):
            raise ValueError("Expected a Path instance to write the objects to.")

        utils.to_json_file(list(self._objs), path)

    def __getitem__(self, index: int) -> object:
        return self.__objs[index]

    def __iter__(self) -> Generator:
        return (obj for obj in self._objs)

    def __str__(self) -> str:
        string = f"Objects ({len(list(self._objs))}):"
        for obj in self._objs:
            string += f"\n  - ({obj.id}) {obj.name}"

        return string
