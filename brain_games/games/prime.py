"""Logic module for brain-prime game."""
import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUMBER = 1000


def _is_prime(num):
    """Do check number is prime.

    Args:
        num (int): Some number

    Returns:
        bool: Returns True if number is prime.
    """
    return all(num % divider != 0 for divider in range(2, num))


def _generate_answer(question):
    prime = _is_prime(question)
    if prime:
        return 'yes'
    return 'no'


def generate_round():
    number = random.randint(0, MAX_NUMBER)
    answer = _generate_answer(number)
    return number, answer
