#!/usr/bin/env python
"""Prime-check game script."""
import random

from brain_games.game_utils import process_all

MAX_NUMBER = 1000


def is_prime(num):
    """Do check number is prime.

    Args:
        num (int): Some number

    Returns:
        bool: Returns True if number is prime.
    """
    return all(num % divider != 0 for divider in range(2, num))


def check_answer(num: int, answer: str) -> bool:
    """Do check player answer.

    Args:
        num (int): Number to check - prime or not.
        answer (str): Player answer 'yes', 'no' or something else.

    Returns:
        bool: Correct or incorrect player answer.
    """
    correct_prime = answer == 'yes' and is_prime(num)
    correct_not_prime = answer == 'no' and not is_prime(num)
    if answer not in ('yes', 'no'):
        print('Incompatible answer')
        return False
    elif correct_prime or correct_not_prime:
        print('Correct!')
        return True
    right_answer = 'yes' if answer == 'no' else 'no'
    print("'{0}' is wrong answer ;(. ".format(answer), end='')
    print("Correct answer was '{0}'.".format(right_answer))
    return False


def generate_question() -> int:
    """Do generate question.

    Returns:
        int: Random number between 0 and max number
    """
    number = random.randint(0, MAX_NUMBER)
    print('Question: {0}'.format(number))
    return number


def main():
    """Do launch and controls prime game."""
    desc = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    process_all(desc, generate_question, check_answer)


if __name__ == '__main__':
    main()
