"""Logic module for brain-calc game."""
import random
from typing import Tuple

DESCRIPTION = 'What is the result of the expression?'
_OPERATORS = ('+', '-', '*')
_LIMIT = 50


def _generate_answer(question: Tuple) -> int:
    """Do generate right answer.

    Args:
        question: Tuple of two numbers and operator between

    Returns:
        int: Result of operation with numbers
    """
    num1, operator, num2 = question
    right_answers = {
        '+': num1 + num2,
        '*': num1 * num2,
        '-': num1 - num2,
    }
    return right_answers[operator]


def generate_round():
    """Do generate question and answer.

    Returns:
        tuple(str, int): String question for print and answer
    """
    question = (
        random.randint(0, _LIMIT),
        random.choice(_OPERATORS),
        random.randint(0, _LIMIT),
    )
    answer = _generate_answer(question)
    string_question = '{0} {1} {2}'.format(*question)

    return string_question, answer
