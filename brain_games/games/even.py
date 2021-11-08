"""Logic module for brain-even game."""
import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_NUMBER = 1000


def _generate_answer(question):
    even = question % 2 == 0
    if even:
        return 'yes'
    return 'no'


def generate_round():
    number = random.randint(0, MAX_NUMBER)
    answer = _generate_answer(number)
    return number, answer
