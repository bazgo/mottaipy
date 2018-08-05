"""
Define the material types.
"""

from abc import ABC


class Material(ABC):
    """
    Parent class for the material types.
    """

    pass


class Paper(Material, ABC):
    """
    Abstract class for the Paper type.
    """

    points = 1


class Cloth(Material, ABC):
    """
    Abstract class for the Cloth type.
    """

    points = 2


class Stone(Material, ABC):
    """
    Abstract class for the Stone type.
    """

    points = 2


class Clay(Material, ABC):
    """
    Abstract class for the Clay type.
    """

    points = 3


class Metal(Material, ABC):
    """
    Abstract class for the Metal type.
    """

    points = 3
