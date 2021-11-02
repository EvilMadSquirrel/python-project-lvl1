#!/usr/bin/env python
"""GCD game script."""
import math
import random

from brain_games.game_utils import process_all


def generate_question():
    """Do generate question for GCD calculation.

    Returns:
        tuple(int): Two random numbers
    """
    limit = 20
    num1 = random.randint(0, limit)
    num2 = random.randint(0, limit)
    q_string = 'Question: {0} {1}'.format(num1, num2)
    print(q_string)
    return num1, num2


def check_answer(question, answer):
    """Do check player answer.

    Args:
        question (tuple): Two random numbers
        answer (str): Player answer

    Returns:
        bool: Correct or incorrect player answer.
    """
    num1, num2 = question
    right_answer = math.gcd(num1, num2)
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
    description = 'Find the greatest common divisor of given numbers.'
    process_all(description, generate_question, check_answer)


if __name__ == '__main__':
    main()
