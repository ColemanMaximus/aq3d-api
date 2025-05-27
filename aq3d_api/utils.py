"""
This module provides a bunch of utils which the other
modules in this package use.
"""
from pathlib import Path
import csv


def to_enum(enum, value, fallback = None):
    """
    Converts an value into an Enum type from the supplied Enum class.

    :param enum: The Enum class to search over.
    :param value: The value of the type within the Enum class.
    :param fallback: If there is no match, return this default value.

    :return: Returns the matched Enum type or fallback if there is no match.
    """

    return next((enum_value for enum_value in enum if enum_value.value == value), fallback)


def to_csv(objs: list, path: Path):
    """
    Creates a csv file in the path supplied with all the objects
    dict keys and values.

    :param objs: A list of objects to save their dict values.
    :param path: The path to write the csv to.
    """

    if not objs:
        raise ValueError(
            "There were no items in the list to write to a csv file."
        )

    if not isinstance(path, Path):
        raise ValueError("Expected a path to save to a csv file.")

    with open(path, "w", newline="") as file:
        writer = csv.writer(file)


        keys = [key.split("__")[-1] for key in objs[0].__dict__.keys()]
        writer.writerow(keys)

        rows = [list(obj.__dict__.values()) for obj in objs]
        writer.writerows(rows)
