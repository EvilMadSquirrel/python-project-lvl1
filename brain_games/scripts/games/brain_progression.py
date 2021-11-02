#!/usr/bin/env python
"""Progression game script."""
import random

from brain_games.game_utils import process_all

max_start = 20


def make_progression():
    """Do generate 'random' progression.

    Returns:
        list(str): Progression
    """
    prog_len = random.randint(5, 10)
    diff = random.randint(2, 10)
    start = random.randint(0, max_start)
    return [str(start + diff * idx) for idx in range(prog_len)]


def generate_question():
    """Do generate question with progression.

    Returns:
        str: Right answer
    """
    prog = make_progression()
    missing_position = random.randint(0, len(prog) - 1)
    missing_element = prog[missing_position]
    prog[missing_position] = '..'

    print('Question: {0}'.format(' '.join(prog)))
    return int(missing_element)


def check_answer(right_answer, answer):
    """Do check player answer.

    Args:
        right_answer (int): Right answer
        answer (str): Player answer

    Returns:
        bool: Correct or incorrect player answer.
    """
    player_answer = 0
    try:
        player_answer = int(answer)
    except ValueError:
        print('Incorrect answer')
        return False
    if player_answer == right_answer:
        print('Correct')
        return True
    print("'{0}' is wrong answer ;(. ".format(player_answer), end='')
    print("Correct answer was '{0}'.".format(right_answer))
    return False


def main():
    """Do launch and controls calc game."""
    description = 'What number is missing in the progression?'
    process_all(description, generate_question, check_answer)


if __name__ == '__main__':
    main()
