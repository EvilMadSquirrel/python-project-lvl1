#!/usr/bin/env python
"""Script runs brain-gcd game."""

from brain_games.game_engine import play_game
from brain_games.games.gcd import DESCRIPTION, check_answer, generate_question


def main():
    """Do launch calc game."""
    play_game(DESCRIPTION, generate_question, check_answer)


if __name__ == '__main__':
    main()
