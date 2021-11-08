#!/usr/bin/env python
"""Script runs brain-calc game."""

from brain_games.game_engine import play_game
from brain_games.games import calc


def main():
    """Do launch calc game."""
    play_game(calc)


if __name__ == '__main__':
    main()
