"""Logic module for brain-gcd game."""
import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
LIMIT = 20


def _calculate_gcd(num1, num2):
    if num2 == 0:
        return num1
    return _calculate_gcd(num2, num1 % num2)


def generate_round():
    num1 = random.randint(0, LIMIT)
    num2 = random.randint(0, LIMIT)
    answer = _calculate_gcd(num1, num2)
    return (num1, num2), answer
