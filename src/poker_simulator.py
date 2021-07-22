"""A simple poker simulator."""

from abc import ABC, abs
from deck import Deck


class Poker(ABC):
    @abstractmethod
    def deal(self) -> None:
        ...

    @abstractmethod
    def resolve(self) -> None:
        ...

    @abstractmethod
    def play(self) -> None:
        ...


class ClassicPoker(Poker):
    def __init__(self, n_players: int) -> None:
        self.n_players = n_players
        self.deck = ...  # TODO
        self.hands = []
        self.deal()

    def deal(self) -> None:
        for i in range(self.n_players):
            hand = [deck.deal_card() for _ in range(5)]
            self.hands.append()

    def resolve(self) -> None:
        ...

    def play(self) -> None:
        ...
