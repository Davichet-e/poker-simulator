"""A simple poker simulator."""

from abc import ABC, abstractmethod
from typing import Tuple

from colorama import Fore, Style, deinit, init

from .deck import Deck
from .hand import Hand


class Poker(ABC):
    def __init__(self, n_players: int) -> None:
        self.n_players = n_players
        self.deck = Deck()
        self.hands = []

    @abstractmethod
    def deal(self) -> None:
        ...

    @abstractmethod
    def resolve(self) -> Hand:
        ...


class ClassicPoker(Poker):
    def deal(self) -> None:
        for i in range(self.n_players):
            hand = Hand(self.deck)
            print(f"The hand of player {i + 1} is: {hand}")
            print(f"Which is a: {hand.play[0].name}\n\n")
            self.hands.append(hand)

    def resolve(self) -> Tuple[int, Hand]:
        """Return a tuple which represents the winning player with its hand"""
        return max(enumerate(self.hands, start=1), key=lambda tuple_: tuple_[1].play)


if __name__ == "__main__":
    init(autoreset=True)
    while True:
        print(f"Be welcome to {Fore.GREEN}Poker Simulator.\n")
        # TODO Ask number of players interactively
        n_players = 3
        print(f"Nº of selected players: {n_players}")
        poker = ClassicPoker(n_players)
        poker.deal()
        winner_player, winner_hand = poker.resolve()
        print(f"The winner is player {winner_player} ({winner_hand})")

        decision: str = input(f"\nDo you want to play another round? (y/n)\n> ")

        if decision.strip().lower() not in {"y", "yes", "1", "true"}:
            break

    print(f"\n{Fore.YELLOW}Thanks for playing!")
    deinit()

