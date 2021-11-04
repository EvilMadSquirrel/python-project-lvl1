#!/usr/bin/env python
"""Script runs brain-calc game."""

from brain_games.game_engine import play_game
from brain_games.games.calc import DESCRIPTION, check_expression, generate_expression


def main():
    """Do launch calc game."""
    play_game(DESCRIPTION, generate_expression, check_expression)


if __name__ == '__main__':
    main()
