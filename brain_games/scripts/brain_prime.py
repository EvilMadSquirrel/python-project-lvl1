#!/usr/bin/env python
"""Script runs brain-prime game."""

from brain_games.game_engine import play_game
from brain_games.games import prime


def main():
    """Do launch prime game."""
    play_game(prime)


if __name__ == '__main__':
    main()
