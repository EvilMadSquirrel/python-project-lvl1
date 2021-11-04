#!/usr/bin/env python
"""Script runs brain-prime game."""

from brain_games.game_engine import play_game
from brain_games.games.prime import DESC, check_answer, generate_question


def main():
    """Do launch prime game."""
    play_game(DESC, generate_question, check_answer)


if __name__ == '__main__':
    main()
