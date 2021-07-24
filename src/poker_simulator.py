"""A simple poker simulator."""

from abc import ABC, abstractmethod

from colorama import Fore, Style, deinit, init

from .deck import Deck
from .hand import Hand


class Poker(ABC):
    @abstractmethod
    def deal(self) -> None:
        ...

    @abstractmethod
    def resolve(self) -> None:
        ...


class ClassicPoker(Poker):
    def __init__(self, n_players: int) -> None:
        self.n_players = n_players
        self.deck = Deck()
        self.hands = []

    def deal(self) -> None:
        for i in range(self.n_players):
            hand = Hand(self.deck)
            print(f"The hand of player {i + 1} is:")
            print(hand)
            print(hand.play)
            self.hands.append(hand)

    def resolve(self) -> Hand:
        return max(self.hands, key=lambda hand: hand.play)


if __name__ == "__main__":
    init(autoreset=True)
    print(f"Be welcomed to {Fore.GREEN}Poker Simulator{Style.RESET_ALL}.")
    n_players = 3
    print(f"Nº of selected players: {n_players}")
    poker = ClassicPoker(n_players)
    poker.deal()
    print(poker.resolve())
    print("test 2")
    deinit()

