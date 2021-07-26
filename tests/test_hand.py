import unittest

from src.deck import Card, Deck
from src.hand import Hand, Kind


class TestKindHand(unittest.TestCase):
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
                    Deck.CardName.ACE,
                    Deck.CardName.TEN,
                    Deck.CardName.FIVE,
                    Deck.CardName.FOUR,
                    Deck.CardName.TWO,
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
                    Deck.CardName.TWO,
                    Deck.CardName.ACE,
                    Deck.CardName.TEN,
                    Deck.CardName.FIVE,
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
                [Deck.CardName.FIVE, Deck.CardName.TWO, Deck.CardName.ACE,],
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
            (Kind.THREE_OF_A_KIND, [Deck.CardName.TWO]),
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
                    Deck.CardName.SIX,
                    Deck.CardName.FIVE,
                    Deck.CardName.FOUR,
                    Deck.CardName.THREE,
                    Deck.CardName.TWO,
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
                    Deck.CardName.ACE,
                    Deck.CardName.TEN,
                    Deck.CardName.SIX,
                    Deck.CardName.FOUR,
                    Deck.CardName.TWO,
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
            (Kind.FULL_HOUSE, [Deck.CardName.TWO]),
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
            (Kind.FOUR_OF_A_KIND, [Deck.CardName.TWO]),
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
                    Deck.CardName.SIX,
                    Deck.CardName.FIVE,
                    Deck.CardName.FOUR,
                    Deck.CardName.THREE,
                    Deck.CardName.TWO,
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
                    Deck.CardName.ACE,
                    Deck.CardName.KING,
                    Deck.CardName.QUEEN,
                    Deck.CardName.JACK,
                    Deck.CardName.TEN,
                ],
            ),
        )


class TestTiedHand(unittest.TestCase):
    def test_pair_tie(self):
        self.assertEqual(
            Hand.calculate_hand_value(
                [
                    Card(Deck.CardName.ACE, "♥"),
                    Card(Deck.CardName.TWO, "♥"),
                    Card(Deck.CardName.TWO, "♣"),
                    Card(Deck.CardName.FIVE, "♦"),
                    Card(Deck.CardName.TEN, "♥"),
                ]
            ),
            Hand.calculate_hand_value(
                [
                    Card(Deck.CardName.ACE, "♦"),
                    Card(Deck.CardName.TWO, "♦"),
                    Card(Deck.CardName.TWO, "♥"),
                    Card(Deck.CardName.FIVE, "♣"),
                    Card(Deck.CardName.TEN, "♦"),
                ]
            ),
        )

    def test_straight_tie(self):
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
            Hand.calculate_hand_value(
                [
                    Card(Deck.CardName.TWO, "♠"),
                    Card(Deck.CardName.THREE, "♦"),
                    Card(Deck.CardName.FOUR, "♦"),
                    Card(Deck.CardName.FIVE, "♦"),
                    Card(Deck.CardName.SIX, "♠"),
                ]
            ),
        )

    def test_flush_tie(self):
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
            Hand.calculate_hand_value(
                [
                    Card(Deck.CardName.TWO, "♠"),
                    Card(Deck.CardName.TEN, "♠"),
                    Card(Deck.CardName.FOUR, "♠"),
                    Card(Deck.CardName.ACE, "♠"),
                    Card(Deck.CardName.SIX, "♠"),
                ]
            ),
        )

    def test_royal_flush_tie(self):
        self.assertEqual(
            Hand.calculate_hand_value(
                [
                    Card(Deck.CardName.TEN, "♣"),
                    Card(Deck.CardName.JACK, "♣"),
                    Card(Deck.CardName.QUEEN, "♣"),
                    Card(Deck.CardName.KING, "♣"),
                    Card(Deck.CardName.ACE, "♣"),
                ]
            ),
            Hand.calculate_hand_value(
                [
                    Card(Deck.CardName.TEN, "♦"),
                    Card(Deck.CardName.JACK, "♦"),
                    Card(Deck.CardName.QUEEN, "♦"),
                    Card(Deck.CardName.KING, "♦"),
                    Card(Deck.CardName.ACE, "♦"),
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
