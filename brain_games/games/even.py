"""Logic module for brain-even game."""
import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
_MAX_NUMBER = 1000


def generate_round():
    """Do generate question and answer.

    Returns:
        tuple(int, str): Number and answer 'yes' or 'no'
    """
    number = random.randint(0, _MAX_NUMBER)
    answer = 'yes' if number % 2 == 0 else 'no'
    return number, answer
