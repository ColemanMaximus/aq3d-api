""" This module contains the DataContainer class."""

from collections.abc import Generator
from pathlib import Path

from aq3d_api import utils


class DataContainer:
    """
    Acts as a container of objects with useful methods to process those
    objects.
    """

    def __init(self, objs):
        """
        :param objs: The objects to add to this container.
        """

        self.objs = objs

    @property
    def _objs(self) -> Generator:
        """
        Gets the objects stored within this data container.

        :return: The stored objects.
        """

        return (obj for obj in self.__objs)

    @_objs.setter
    def _objs(self, objs):
        """
        Sets the objects for this data container instance.

        :param objs: The objects to add to this container.
        """

        self.__objs = objs

    def add(self, obj, cls):
        """
        Adds a Server object into the Servers instance.

        :param server: The Server object to add into the Servers container.
        """

        if not isinstance(obj, cls):
            raise ValueError(
                f"Expected a {type(cls)} object but instead received {type(obj)}."
            )

        if self._objs:
            objs = list(self._objs)
            objs.append(obj)
            self._objs = objs

    def to_csv(self, path: Path):
        """
        Useful method to export all the objects within this data container
        into a csv file.

        :param path: The path to write the objects to.
        """

        if not isinstance(path, Path):
            raise ValueError("Expected a Path instance to write the objects to.")

        utils.to_csv(list(self._objs), path)

    def to_json_file(self, path: Path):
        """
        Useful method to export all the objects within this data container
        into a json file.

        :param path: The path to write the objects to.
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
