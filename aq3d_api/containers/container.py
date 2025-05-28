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

    def __init__(self, objs):
        """
        Parameters:
            objs: List of objects to store in the container.
        """

        self.objs = objs

    @property
    def _objs(self) -> Generator:
        """
        Returns a generator that yields all objects stored in the container.

        Yields:
            Generator: Each object contained within the container.
        """

        return (obj for obj in self.__objs)

    @_objs.setter
    def _objs(self, objs):
        """
        Sets the internal list of objects for the container.

        Parameters:
            objs (Iterable): The collection of objects to be stored in the container.
        """

        self.__objs = objs

    def add(self, obj, cls):
        """
        Adds an object to the container if it is an instance of the specified class_

        Parameters:
            obj (Any): The object to be added to the container.
            cls (type): The class or type that `obj` is expected to be an instance of.

        Raises:
            ValueError: If `obj` is not an instance of `cls`.
        """

        if not isinstance(obj, cls):
            raise ValueError(
                f"Expected a {type(cls)} object but instead received {type(obj)}."
            )

        if self.__objs:
            self.__objs.append(obj)

    def to_csv(self, path: Path):
        """
        Export the objects contained in this container to a CSV file.

        This method serializes the objects stored in the container
        and writes them to the specified CSV file.

        Args:
            path (Path): The file path where the CSV will be saved.

        Raises:
            ValueError: If the provided path is not an instance of pathlib.Path.
        """

        if not isinstance(path, Path):
            raise ValueError("Expected a Path instance to write the objects to.")

        utils.to_csv(list(self._objs), path)

    def to_json_file(self, path: Path):
        """
        Serializes the container's objects to a JSON file at the specified path.

        Args:
            path (Path): The file system path where the JSON file will be written.

        Raises:
            ValueError: If the provided path is not an instance of pathlib.Path.
        """

        if not isinstance(path, Path):
            raise ValueError("Expected a Path instance to write the objects to.")

        utils.to_json_file(list(self._objs), path)

    def __getitem__(self, index: int):
        return list(self._objs)[index]

    def __iter__(self) -> Generator:
        return (obj for obj in self._objs)

    def __str__(self) -> str:
        string = f"Objects ({len(list(self._objs))}):"
        for obj in self._objs:
            string += f"\n  - ({obj.id}) {obj.name}"

        return string
