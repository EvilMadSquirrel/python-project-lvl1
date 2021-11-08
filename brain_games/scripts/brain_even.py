#!/usr/bin/env python
"""Script runs brain-even game."""

from brain_games.game_engine import play_game
from brain_games.games import even


def main():
    """Do launch even game."""
    play_game(even)


if __name__ == '__main__':
    main()
