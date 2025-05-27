"""
This module provides a bunch of utils which the other
modules in this package use.
"""
import json
import csv

from json import JSONDecodeError
from pathlib import Path
from enum import Enum


class EnumEncoder(json.JSONEncoder):
    """
    A JSONEncoder class for encoding Enum types by
    returning their names instead.
    """

    def default(self, o):
        if isinstance(o, Enum):
            return o.name

        return None


def to_enum(enum, value, fallback = None):
    """
    Converts a value into an Enum type from the supplied Enum class.

    :param enum: The Enum class to search over.
    :param value: The value of the type within the Enum class.
    :param fallback: If there is no match, return this default value.

    :return: Returns the matched Enum type or fallback if there is no match.
    """

    return next((enum_value for enum_value in enum if enum_value.value == value), fallback)


def to_dict(obj) -> dict:
    """
    Converts an object to a dict representation.

    :param obj: The object to covert to a dict.
    :return: The new dict object from the attributes of the object.
    """

    # Filter any redundant keypair values from the object dict.
    filtered_dict = {
        key.split("__")[-1]: value
        for key, value in obj.__dict__.items() if value
    }

    return filtered_dict


def to_csv(objs: list, path: Path):
    """
    Creates a csv file in the path supplied with all the objects
    dict keys and values.

    :param objs: A list of objects to save their dict values.
    :param path: The path to write the csv data to.
    """

    if not objs:
        raise ValueError(
            "There were no objects in the list to write to a csv file."
        )

    if not isinstance(path, Path):
        raise ValueError("Expected a path to save to a csv file.")

    with open(path, "w", newline="") as file:
        writer = csv.writer(file)

        keys = [key.split("__")[-1] for key in objs[0].__dict__.keys()]
        writer.writerow(keys)

        rows = [list(obj.__dict__.values()) for obj in objs]
        writer.writerows(rows)


def to_json_file(objs: list, path: Path):
    """
        Creates a json file in the path supplied with all the objects
        dict keys and values.

        :param objs: A list of objects to save their dict values.
        :param path: The path to write the json data to.
        """

    if not objs:
        raise ValueError(
            "There were no objects in the list to write to a json file."
        )

    if not isinstance(path, Path):
        raise ValueError("Expected a path to save to a json file.")

    try:
        dict_objects = [
            obj.to_dict() if obj.__getattribute__("to_dict")
                          else obj.__dict__ for obj in objs
        ]

        path.write_text(json.dumps(dict_objects, indent=4, cls=EnumEncoder))
    except JSONDecodeError as ex:
        raise ex
