#!/usr/bin/env python
"""Script runs brain-even game."""

from brain_games.game_engine import play_game
from brain_games.games.even import DESCRIPTION, check_answer, generate_question


def main():
    """Do launch even game."""
    play_game(DESCRIPTION, generate_question, check_answer)


if __name__ == '__main__':
    main()
