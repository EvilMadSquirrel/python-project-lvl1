"""Logic module for brain-even game."""
import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
_MAX_NUMBER = 1000


def _generate_answer(question: int) -> str:
    """Do generate right answer.

    Args:
        question: Number may be even or odd

    Returns:
        str: 'yes' if number is even, else 'no'
    """
    even = question % 2 == 0
    if even:
        return 'yes'
    return 'no'


def generate_round():
    """Do generate question and answer.

    Returns:
        tuple(int, str): Number and answer 'yes' or 'no'
    """
    number = random.randint(0, _MAX_NUMBER)
    answer = _generate_answer(number)
    return number, answer
