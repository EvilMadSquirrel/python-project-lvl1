#!/usr/bin/env python
"""Script runs brain-calc game."""

from brain_games import games, game_engine


def main():
    """Do launch calc game."""
    game_engine.play_game(games.calc)


if __name__ == '__main__':
    main()
