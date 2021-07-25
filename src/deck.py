from __future__ import annotations

import random
from enum import Enum, IntEnum, auto
from typing import ClassVar, Dict, List, NamedTuple, Tuple

from colorama import Fore, Style


class Card(NamedTuple):
    name: Deck.CardName
    suit: str

    def __str__(self) -> str:
        return f"{self.name.name} of {self.suit}"

    @property
    def value(self) -> int:
        return self.name.value


class Deck:
    """Implement a standard 52-card deck."""

    class Suit(Enum):
        CLUBS = "♣"
        HEARTS = "♥"
        PIKES = "♠"
        DIAMONDS = "♦"

    class CardName(IntEnum):
        TWO = auto()
        THREE = auto()
        FOUR = auto()
        FIVE = auto()
        SIX = auto()
        SEVEN = auto()
        EIGHT = auto()
        NINE = auto()
        TEN = auto()
        JACK = auto()
        QUEEN = auto()
        KING = auto()
        ACE = auto()

    def __init__(self):
        self._deck: List[Card] = [
            Card(card, suit.value) for suit in Deck.Suit for card in Deck.CardName
        ]
        random.shuffle(self._deck)

    def __len__(self):
        return len(self._deck)

    def __getitem__(self, position: int) -> Card:
        return self._deck[position]

    def deal_card(self) -> Card:
        """Returns a random card of the deck."""
        # If the deck is empty, initialize it
        if not self._deck:
            print(f"Deck {Fore.RED}empty{Style.RESET_ALL}, shuffling a new one.")
            self.__init__()
        return self._deck.pop()
