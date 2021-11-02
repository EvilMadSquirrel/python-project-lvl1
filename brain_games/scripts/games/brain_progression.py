#!/usr/bin/env python
"""Progression game script."""
import random

from brain_games.game_utils import process_all


def generate_progression():
    """Do generate arithmetic progression.

    Returns:
        int: Right answer
    """
    prog_len = random.randint(5, 10)
    diff = random.randint(2, 10)
    missing_position = random.randint(0, prog_len - 1)
    start = random.randint(0, 20)
    prog = [start + diff * i for i in range(prog_len)]
    missing_element = prog[missing_position]
    prog[missing_position] = '..'
    q_string = 'Question: {0}'.format(' '.join(str(thing) for thing in prog))
    print(q_string)
    return missing_element


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
    process_all(description, generate_progression, check_answer)


if __name__ == '__main__':
    main()
