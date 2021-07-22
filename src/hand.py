from collections import Counter
from enum import IntEnum, auto
from functools import total_ordering
from typing import Tuple
from deck import Deck


class Kind(IntEnum):
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


@total_ordering
class Hand:
    def __init__(self, deck: Deck) -> None:
        self.cards = [deck.deal_card() for _ in range(5)]
        self.play: Tuple[Kind, int] = Hand.calculate_points(self.cards)

    def __gt__(self, other: Hand) -> bool:
        return self.play > other.play

    def __eq__(self, other: Hand):
        return self.play == other.play

    @staticmethod
    def calculate_points(cards: List[Card]) -> Tuple[Kind, int]:
        card_values = [card.value for card in cards]
        min_card_value = min(card_values)
        max_card_value = max(card_values)

        suit_counter = Counter([card.suit for card in cards])
        name_counter = Counter([card.name for card in cards])

        most_common = name_counter.most_common(1)[0][1]

        kind: Kind
        # We compare how many kinds of card are there
        if len(name_counter) == 2:
            # If the most common element appears 4 times, then is a `four of a kind`
            if most_common == 4:
                kind = Kind.FOUR_OF_A_KIND

            else:
                kind = Kind.FULL_HOUSE

        elif len(name_counter) == 3:
            if most_common == 3:
                kind = Kind.THREE_OF_A_KIND

            else:
                kind = Kind.DOUBLE_PAIR

        elif len(name_counter) == 4:
            kind = Kind.PAIR

        else:
            straight = {-1} == {x[1] - x[0] for x in zip(card_values[1:], card_values)}
            if len(suit_counter) == 1:
                if min_card_value.name == "10":
                    kind = Kind.ROYAL_FLUSH

                elif straight:
                    kind = Kind.STRAIGHT_FLUSH

                else:
                    kind = Kind.FLUSH

            elif straight:
                kind = Kind.STRAIGHT

            else:
                kind = Kind.HIGH_CARD

        # FIXME I think the max card is only from the cards forming the kind of hand
        return (kind, max_card_value)
