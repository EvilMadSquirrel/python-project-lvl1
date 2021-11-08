#!/usr/bin/env python
"""Script runs brain-progression game."""

from brain_games.game_engine import play_game
from brain_games.games import progression


def main():
    """Do launch progression game."""
    play_game(progression)


if __name__ == '__main__':
    main()
