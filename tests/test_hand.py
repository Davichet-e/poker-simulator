import unittest

from src.deck import Card, Deck
from src.hand import Hand, Kind


class TestHand(unittest.TestCase):
    def test_high_card(self):
        self.assertEqual(
            Hand.calculate_hand_value(
                [
                    Card(Deck.CardName.ACE, "♦"),
                    Card(Deck.CardName.TWO, "♦"),
                    Card(Deck.CardName.FOUR, "♣"),
                    Card(Deck.CardName.FIVE, "♣"),
                    Card(Deck.CardName.TEN, "♦"),
                ]
            ),
            (
                Kind.HIGH_CARD,
                [
                    Card(Deck.CardName.ACE, "♦").value,
                    Card(Deck.CardName.TEN, "♦").value,
                    Card(Deck.CardName.FIVE, "♣").value,
                    Card(Deck.CardName.FOUR, "♣").value,
                    Card(Deck.CardName.TWO, "♦").value,
                ],
            ),
        )

    def test_pair(self):
        self.assertEqual(
            Hand.calculate_hand_value(
                [
                    Card(Deck.CardName.ACE, "♦"),
                    Card(Deck.CardName.TWO, "♦"),
                    Card(Deck.CardName.TWO, "♥"),
                    Card(Deck.CardName.FIVE, "♣"),
                    Card(Deck.CardName.TEN, "♦"),
                ]
            ),
            (
                Kind.PAIR,
                [
                    Card(Deck.CardName.TWO, "♦").value,
                    Card(Deck.CardName.ACE, "♦").value,
                    Card(Deck.CardName.TEN, "♦").value,
                    Card(Deck.CardName.FIVE, "♣").value,
                ],
            ),
        )

    def test_double_pair(self):
        self.assertEqual(
            Hand.calculate_hand_value(
                [
                    Card(Deck.CardName.ACE, "♦"),
                    Card(Deck.CardName.TWO, "♦"),
                    Card(Deck.CardName.TWO, "♣"),
                    Card(Deck.CardName.FIVE, "♣"),
                    Card(Deck.CardName.FIVE, "♠"),
                ]
            ),
            (
                Kind.DOUBLE_PAIR,
                [
                    Card(Deck.CardName.FIVE, "♣").value,
                    Card(Deck.CardName.TWO, "♦").value,
                    Card(Deck.CardName.ACE, "♦").value,
                ],
            ),
        )

    def test_three_of_a_kind(self):
        self.assertEqual(
            Hand.calculate_hand_value(
                [
                    Card(Deck.CardName.ACE, "♦"),
                    Card(Deck.CardName.TWO, "♦"),
                    Card(Deck.CardName.TWO, "♣"),
                    Card(Deck.CardName.TWO, "♠"),
                    Card(Deck.CardName.FIVE, "♠"),
                ]
            ),
            (Kind.THREE_OF_A_KIND, [Card(Deck.CardName.TWO, "♦").value,],),
        )

    def test_straight(self):
        self.assertEqual(
            Hand.calculate_hand_value(
                [
                    Card(Deck.CardName.TWO, "♦"),
                    Card(Deck.CardName.THREE, "♣"),
                    Card(Deck.CardName.FOUR, "♣"),
                    Card(Deck.CardName.FIVE, "♠"),
                    Card(Deck.CardName.SIX, "♦"),
                ]
            ),
            (
                Kind.STRAIGHT,
                [
                    Card(Deck.CardName.SIX, "♦").value,
                    Card(Deck.CardName.FIVE, "♠").value,
                    Card(Deck.CardName.FOUR, "♣").value,
                    Card(Deck.CardName.THREE, "♣").value,
                    Card(Deck.CardName.TWO, "♦").value,
                ],
            ),
        )

    def test_flush(self):
        self.assertEqual(
            Hand.calculate_hand_value(
                [
                    Card(Deck.CardName.TWO, "♦"),
                    Card(Deck.CardName.TEN, "♦"),
                    Card(Deck.CardName.FOUR, "♦"),
                    Card(Deck.CardName.ACE, "♦"),
                    Card(Deck.CardName.SIX, "♦"),
                ]
            ),
            (
                Kind.FLUSH,
                [
                    Card(Deck.CardName.ACE, "♦").value,
                    Card(Deck.CardName.TEN, "♦").value,
                    Card(Deck.CardName.SIX, "♦").value,
                    Card(Deck.CardName.FOUR, "♦").value,
                    Card(Deck.CardName.TWO, "♦").value,
                ],
            ),
        )

    def test_full_house(self):
        self.assertEqual(
            Hand.calculate_hand_value(
                [
                    Card(Deck.CardName.TWO, "♥"),
                    Card(Deck.CardName.TWO, "♦"),
                    Card(Deck.CardName.TWO, "♣"),
                    Card(Deck.CardName.FIVE, "♣"),
                    Card(Deck.CardName.FIVE, "♠"),
                ]
            ),
            (Kind.FULL_HOUSE, [Card(Deck.CardName.TWO, "♣").value,],),
        )

    def test_four_of_a_kind(self):
        self.assertEqual(
            Hand.calculate_hand_value(
                [
                    Card(Deck.CardName.TWO, "♥"),
                    Card(Deck.CardName.TWO, "♦"),
                    Card(Deck.CardName.TWO, "♣"),
                    Card(Deck.CardName.TWO, "♠"),
                    Card(Deck.CardName.FIVE, "♠"),
                ]
            ),
            (Kind.FOUR_OF_A_KIND, [Card(Deck.CardName.TWO, "♦").value,],),
        )

    def test_straight_flush(self):
        self.assertEqual(
            Hand.calculate_hand_value(
                [
                    Card(Deck.CardName.TWO, "♦"),
                    Card(Deck.CardName.THREE, "♦"),
                    Card(Deck.CardName.FOUR, "♦"),
                    Card(Deck.CardName.FIVE, "♦"),
                    Card(Deck.CardName.SIX, "♦"),
                ]
            ),
            (
                Kind.STRAIGHT_FLUSH,
                [
                    Card(Deck.CardName.SIX, "♦").value,
                    Card(Deck.CardName.FIVE, "♦").value,
                    Card(Deck.CardName.FOUR, "♦").value,
                    Card(Deck.CardName.THREE, "♦").value,
                    Card(Deck.CardName.TWO, "♦").value,
                ],
            ),
        )

    def test_royal_flush(self):
        self.assertEqual(
            Hand.calculate_hand_value(
                [
                    Card(Deck.CardName.TEN, "♦"),
                    Card(Deck.CardName.JACK, "♦"),
                    Card(Deck.CardName.QUEEN, "♦"),
                    Card(Deck.CardName.KING, "♦"),
                    Card(Deck.CardName.ACE, "♦"),
                ]
            ),
            (
                Kind.ROYAL_FLUSH,
                [
                    Card(Deck.CardName.ACE, "♦").value,
                    Card(Deck.CardName.KING, "♦").value,
                    Card(Deck.CardName.QUEEN, "♦").value,
                    Card(Deck.CardName.JACK, "♦").value,
                    Card(Deck.CardName.TEN, "♦").value,
                ],
            ),
        )


if __name__ == "__main__":
    unittest.main()
