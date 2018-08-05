"""
Define the abstract Card class.
"""

from abc import ABC, abstractmethod

from mottaipy.materials import Material, Paper, Cloth, Stone, Clay, Metal


class Card(ABC):
    """
    Representation of a card in the deck.
    """

    def __init__(self, name: str, material: Material):
        self.name = name
        self.material = material

    @property
    def points(self) -> int:
        return self.material.points

