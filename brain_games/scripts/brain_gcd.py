#!/usr/bin/env python
"""Script runs brain-gcd game."""

from brain_games.game_engine import play_game
from brain_games.games import gcd


def main():
    """Do launch calc game."""
    play_game(gcd)


if __name__ == '__main__':
    main()
