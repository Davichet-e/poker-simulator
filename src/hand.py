from __future__ import annotations

from collections import Counter
from enum import IntEnum, auto
from functools import total_ordering
from typing import List, Tuple

from .deck import Card, Deck


class Kind(IntEnum):
    """Represent the Kind that the Hand is, ranked by value"""

    HIGH_CARD = auto()
    PAIR = auto()
    DOUBLE_PAIR = auto()
    THREE_OF_A_KIND = auto()
    STRAIGHT = auto()
    FLUSH = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    STRAIGHT_FLUSH = auto()
    ROYAL_FLUSH = auto()

    def __repr__(self) -> str:
        return self.name


@total_ordering
class Hand:
    def __init__(self, deck: Deck) -> None:
        self._cards: List[Card] = [deck.deal_card() for _ in range(5)]
        self._play: Tuple[Kind, List[int]] = Hand.calculate_hand_value(self.cards)

    @property
    def cards(self) -> List[Card]:
        return self._cards

    @property
    def play(self) -> Tuple[Kind, List[int]]:
        """Returns a tuple representing what kind is the hand and the important cards in case of a draw"""
        return self._play

    def __gt__(self, other: Hand) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented
        return self.play > other.play

    def __eq__(self, other: Hand) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented
        return self.play == other.play

    def __str__(self) -> str:
        cards_as_str: List[str] = [f"{card}" for card in self.cards]
        return ", ".join(cards_as_str)

    @staticmethod
    def calculate_hand_value(cards: List[Card]) -> Tuple[Kind, List[int]]:
        """Returns which kind the hand is and the necessary cards' values to break the tie if necessary"""
        sorted_card_values = sorted([card.value for card in cards], reverse=True)
        min_card_value = sorted_card_values[-1]

        suit_counter: Counter[str] = Counter([card.suit for card in cards])
        name_counter: Counter[Card] = Counter([card.name for card in cards])

        most_common_cards: List[Tuple[Deck.CardName, int]] = name_counter.most_common(5)
        most_common_card, n_occurrences_most_common = most_common_cards[0]
        # This helps to decide given a draw (e.g. given two different three of a kind), which would win.
        # See this: https://www.pokerhands.com/poker_hand_tie_rules.html
        hand_cards_value: List[int]

        kind: Kind
        # We compare how many kinds of card are there
        if len(name_counter) == 2:
            # If the most common element appears 4 times, then is a `four of a kind`
            if n_occurrences_most_common == 4:
                kind = Kind.FOUR_OF_A_KIND
            else:
                kind = Kind.FULL_HOUSE

            hand_cards = [most_common_card.value]

        elif len(name_counter) == 3:
            if n_occurrences_most_common == 3:
                kind = Kind.THREE_OF_A_KIND
                hand_cards = [most_common_card.value]

            else:
                kind = Kind.DOUBLE_PAIR
                # This checks first the highest cards of the pairs, and then of the non-matching card
                hand_cards = sorted(
                    [card.value for card, _ in most_common_cards[:2]], reverse=True
                ) + [most_common_cards[2][0].value]

        elif len(name_counter) == 4:
            kind = Kind.PAIR

            hand_cards = [
                most_common_card.value,
                *sorted(
                    set(sorted_card_values) - {most_common_card.value}, reverse=True
                ),
            ]

        else:
            # This checks the cards are increasingly monotonic by 1
            straight = {1} == {
                x[1] - x[0] for x in zip(sorted_card_values[1:], sorted_card_values)
            }
            if len(suit_counter) == 1:
                # This checks that the minimum card is 10, so it must mean that the rest of the values form a royal flush
                if min_card_value == 9:
                    kind = Kind.ROYAL_FLUSH

                elif straight:
                    kind = Kind.STRAIGHT_FLUSH

                else:
                    kind = Kind.FLUSH

            elif straight:
                kind = Kind.STRAIGHT

            else:
                kind = Kind.HIGH_CARD

            hand_cards = sorted_card_values

        return (kind, hand_cards)
