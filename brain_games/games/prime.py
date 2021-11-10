"""Logic module for brain-prime game."""
import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
_MAX_NUMBER = 1000


def _is_prime(num):
    """Do check number is prime.

    Args:
        num (int): Some number

    Returns:
        bool: Returns True if number is prime.
    """
    return all(num % divider != 0 for divider in range(2, num))


def generate_round():
    """Do generate question and answer.

    Returns:
        tuple(int, str): Number and answer 'yes' or 'no'
    """
    number = random.randint(0, _MAX_NUMBER)
    answer = 'yes' if _is_prime(number) else 'no'
    return number, answer
