""" This module contains the DataContainer class."""

from collections.abc import Generator
from pathlib import Path

from aq3d_api import utils


class DataContainer:
    def __init(self, objs):
        self.objs = objs

    @property
    def _objs(self) -> Generator:
        return (obj for obj in self.__objs)

    @_objs.setter
    def _objs(self, objs):
        self.__objs = objs

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

    def __iter__(self) -> Generator:
        return (obj for obj in self._objs)

    def __str__(self) -> str:
        string = f"Objects ({len(list(self._objs))}):"
        for obj in self._objs:
            string += f"\n  - ({obj.id}) {obj.name}"

        return string
