"""Logic module for brain-calc game."""
import operator
import random

DESCRIPTION = 'What is the result of the expression?'
_operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}
_LIMIT = 50


def generate_round():
    """Do generate question and answer.

    Returns:
        tuple(str, int): String question for print and answer
    """
    num1 = random.randint(0, _LIMIT)
    random_operator = str(random.choice(list(_operators.keys())))
    num2 = random.randint(0, _LIMIT)

    answer = _operators.get(random_operator)(num1, num2)
    string_question = '{0} {1} {2}'.format(num1, random_operator, num2)

    return string_question, answer
