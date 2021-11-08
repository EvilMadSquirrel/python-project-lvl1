"""Logic module for brain-gcd game."""
import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
LIMIT = 20


def _calculate_gcd(num1: int, num2: int) -> int:
    """Do calculate GCD of two numbers.

    Args:
        num1 (int): First number
        num2 (int): Second number

    Returns:
        int: Greatest common divisor of two numbers
    """
    if num2 == 0:
        return num1
    return _calculate_gcd(num2, num1 % num2)


def generate_round():
    """Do generate question and answer.

    Returns:
        tuple(str, int): String question for print and answer
    """
    num1 = random.randint(0, LIMIT)
    num2 = random.randint(0, LIMIT)
    answer = _calculate_gcd(num1, num2)
    string_question = '{0} {1}'.format(num1, num2)
    return string_question, answer
