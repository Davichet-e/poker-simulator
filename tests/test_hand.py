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
                    Card(Deck.CardName.TWO, "♦"),
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

    # def test_double_pair(self):
    # ... TODO

    # def test_three_of_a_kind(self):
    # ... TODO

    # def test_straight(self):
    # ... TODO

    # def test_flush(self):
    # ... TODO

    # def test_full_house(self):
    # ... TODO

    # def test_four_of_a_kind(self):
    # ... TODO

    # def test_straight_flush(self):
    # ... TODO

    # def test_royal_flush(self):
    # ... TODO


if __name__ == "__main__":
    unittest.main()
