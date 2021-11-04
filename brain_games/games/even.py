"""Logic module for brain-even game."""
import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

MAX_NUMBER = 1000


def check_answer(num: int, answer: str) -> bool:
    """Do check player answer.

    Args:
        num (int): Number to check - even or not.
        answer (str): Player answer 'yes', 'no' or something else.

    Returns:
        bool: Correct or incorrect player answer.
    """
    correct_even = answer == 'yes' and num % 2 == 0
    correct_odd = answer == 'no' and num % 2 != 0
    if answer not in ('yes', 'no'):
        print('Incompatible answer')
        return False
    elif correct_even or correct_odd:
        print('Correct!')
        return True
    right_answer = 'yes' if answer == 'no' else 'no'
    print("'{0}' is wrong answer ;(. ".format(answer), end='')
    print("Correct answer was '{0}'.".format(right_answer))
    return False


def generate_question() -> int:
    """Do generate question.

    Returns:
        int: Random number between 0 and 1000
    """
    number = random.randint(0, MAX_NUMBER)
    print('Question: {0}'.format(number))
    return number
