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
    """Do generate right answer.

    Args:
        question: Number may be prime or not

    Returns:
        str: 'yes' if number is prime, else 'no'
    """
    prime = _is_prime(question)
    if prime:
        return 'yes'
    return 'no'


def generate_round():
    """Do generate question and answer.

    Returns:
        tuple(int, str): Number and answer 'yes' or 'no'
    """
    number = random.randint(0, MAX_NUMBER)
    answer = _generate_answer(number)
    return number, answer
