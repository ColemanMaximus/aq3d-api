"""
This module provides a bunch of utils which the other
modules in this package use.
"""

def to_enum(enum, value, fallback = None):
    """
    Converts an value into an Enum type from the supplied Enum class.

    :param enum: The Enum class to search over.
    :param value: The value of the type within the Enum class.
    :param fallback: If there is no match, return this default value.

    :return: Returns the matched Enum type or fallback if there is no match.
    """

    return next((enum_value for enum_value in enum if enum_value.value == value), fallback)