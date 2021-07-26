"""A simple poker simulator."""

from abc import ABC, abstractmethod
from typing import Tuple, List

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
    def resolve(self) -> Tuple[int, Hand]:
        ...


class ClassicPoker(Poker):
    def deal(self) -> None:
        for i in range(self.n_players):
            hand = Hand(self.deck)
            print(f"The hand of player {i + 1} is: {hand}")
            print(f"Which is a: {hand.play[0].name}\n\n")
            self.hands.append(hand)

    def resolve(self) -> Tuple[Tuple[int, Hand], List[int]]:
        """Return a tuple which represents the winning player with its hand
        and a list with the players that have tied with"""
        sorted_hands = sorted(
            enumerate(self.hands, start=1),
            key=lambda tuple_: tuple_[1].play,
            reverse=True,
        )
        tied_players = []
        for player, hand in sorted_hands[1:]:
            if hand == sorted_hands[0][1]:
                tied_players.append(player)
            else:
                break
        return (sorted_hands[0], tied_players)


if __name__ == "__main__":
    init(autoreset=True)
    print(f"Be welcome to {Fore.GREEN}Poker Simulator.\n")
    while True:

        n_players: int
        while True:
            try:
                n_players = int(
                    input("\nHow many players are going to play? (1-10)\n> ")
                )

            except ValueError:
                print("Please, use only integer values.\n")

            else:
                if 0 < n_players <= 10:
                    break
                else:
                    print("Please, only 1-10 players")

        print(f"\nNº of selected players: {n_players}\n")

        poker = ClassicPoker(n_players)
        poker.deal()
        (winner_player, winner_hand), tied_players = poker.resolve()
        if tied_players:
            print(
                f"There is a draw between players: {', '.join([str(winner_player)] + list(map(str, tied_players)))}"
            )
        else:
            print(
                f"The winner is player {winner_player} ({winner_hand}) [{winner_hand.play[0].name}]"
            )

        decision: str = input(f"\nDo you want to play another round? (y/n)\n> ")

        if decision.strip().lower() not in {"y", "yes", "1", "true"}:
            break

    print(f"\n{Fore.YELLOW}Thanks for playing!")
    deinit()

