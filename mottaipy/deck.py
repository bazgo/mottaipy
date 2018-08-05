from collections import deque
import random
from typing import Iterable, List

from mottaipy.card import Card
from mottaipy.cards import ALL_CARDS


class Deck:
    """
    TODO
    """

    def __init__(self, seed=None):
        # NOTE: the right side of the deque is considered the "top". Draw cards
        # from the right of the deque, and when adding cards to the bottom
        # append to the left of the deque.
        self.deck = deque(ALL_CARDS)
        random.seed(seed)
        self._randstate = random.getstate()

    def shuffle(self):
        """Randomize the order of cards in the deck and return the instance."""
        self.deck = deque(random.shuffle(list(self.deck)))
        return self

    def draw(self) -> Card:
        """Draw the top card of the deck."""
        return self.deck.pop()

    def draw_cards(self, n_cards: int) -> List[Card]:
        """Draw the top card of the deck."""
        return [self.deck.pop() for _ in range(n_cards)]

    def replace(self, cards: Iterable[Card]):
        """Replace cards to the bottom of the deck and return the instance."""
        self.deck.extendleft(cards)
        return self
